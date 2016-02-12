import os

from mimetypes import guess_type

from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.core.servers.basehttp import FileWrapper
from django.db.models import Q


# Create your views here.

from digitalmarket.mixins import (
	MultiSlugMixin,
	SubmitBtnMixin,
	LoginRequiredMixin
)


from .forms import ProductAddForm, ProductModelForm
from .mixins import ProductManagerMixin
from .models import Product


# class SubmitBtnMixin(object):




class ProductDownloadView(MultiSlugMixin, DetailView):
	model = Product

	def get(self, request, *args, **kwargs):
		obj = self.get_object()
		if obj in request.user.myproducts.products.all():
			filepath = os.path.join(settings.PROTECTED_ROOT, obj.media.path)
			guessed_type = guess_type(filepath)[0]

			f = open(filepath, 'rb')
			wrapper = FileWrapper(f)

			mimetype = 'application/force-download'
			if guessed_type:
				mimetype = guessed_type
			response = HttpResponse(wrapper, content_type=mimetype)

			if not request.GET.get("preview"):
				response["Content-Disposition"] = "attachment; filename=%s" %(obj.media.name)

			response["X-SendFile"] = str(obj.media.name)
			return response
		else:
			raise Http404




class ProductCreateView(LoginRequiredMixin, SubmitBtnMixin, CreateView):
	model = Product
	template_name = "form.html"
	form_class = ProductModelForm
	#success_url = "/products/"
	submit_btn = "Add Product"

	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		valid_data = super(ProductCreateView, self).form_valid(form)
		form.instance.managers.add(user)
		# add all default users
		return valid_data

	# def get_success_url(self):
	# 	return reverse("products:list")




class ProductUpdateView(ProductManagerMixin, SubmitBtnMixin, MultiSlugMixin, UpdateView):

	model = Product
	template_name = "form.html"
	form_class = ProductModelForm
	success_url = "/products/"
	submit_btn = "Update Product"

	# def get_object(self, *args, **kwargs):
	#     user = self.request.user
	#     print(user)
	#     obj = super(ProductUpdateView, self).get_object(*args, **kwargs)
	#     print("obj", obj)
	#     if obj.user == user or user in obj.managers.all():
	#         return obj
	#     else:
	#         raise Http404



class ProductDetailView(MultiSlugMixin, DetailView):
	model = Product

	# def get_object(self, *args, **kwargs):
	#     slug = self.kwargs.get("slug")
	#     ModelClass = self.model
	#     print (slug)
	#     if slug is not None:
	#         try:
	#             obj = get_object_or_404(ModelClass, slug=slug)
	#         except ModelClass.MultipleObjectsReturned:
	#             obj = ModelClass.objects.filter(slug=slug).order_by("-title").first()
	#     else:
	#         obj = super(ProductDetailView, self).get_context_data(**kwargs)
	#
	#     return obj

class ProductListView(ListView):


	model = Product

	def get_queryset(self, *args, **kwargs):
		qs = super(ProductListView, self).get_queryset(**kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = qs.filter(
					Q(title__icontains=query)|
					Q(description__icontains=query)
				).order_by("title")
		return qs

	# template_name = "list_view.html"
	# def get_context_data(self, **kwargs):
	#     context = super(ProductListView, self).get_context_data(**kwargs)
	#     print(context)
	#     context["queryset"] = self.get_queryset()
	#     return context

	def get_queryset(self, *args, **kwargs):
		qs =  super(ProductListView, self).get_queryset(**kwargs)
		# qs =  qs.filter(title__icontains="aaaaaa")
		return qs






def create_view(request):
	# Form
	form = ProductModelForm(request.POST or None)


	if form.is_valid():
		print(form.cleaned_data.get("publish"))
		instance = form.save(commit=False)
		instance.sale_price = instance.price
		form.save()

	template = "form.html"
	context = {
		"form": form,
		"submit_btn": "Save Product"
	}
	return render(request, template, context)

def update_view(request, object_id=None):
	product = get_object_or_404(Product, id=object_id)
	form = ProductModelForm(request.POST or None, instance=product)
	if form.is_valid():
		instance = form.save(commit=False)
		form.save()


	template = "form.html"
	context = {
		# "object": product,
		"form": form,
		"submit_btn": "Update Product"
	}
	return render(request, template, context)


def detail_slug_view(request, slug=None):
	try:
		product = get_object_or_404(Product, slug=slug)
	except Product.MultipleObjectsReturned:
		product = Product.objects.filter(slug=slug).order_by("-title").first()

	# print(slug)
	# product = 1
	template = "detail_view.html"
	context = {
		"object": product
	}
	return render(request, template, context)



def detail_view(request, object_id=None):
	product = get_object_or_404(Product, id=object_id)

	template = "detail_view.html"
	context = {
		"object": product
	}
	return render(request, template, context)
	# if object_id is not None:

		# try:
		#     product = Product.objects.get(id=object_id)
		# except Product.DoesNotExist:
		#     product = None
		# template = "detail_view.html"
		# context = {
		#     "object": product
		# }
		# return render(request, template, context)
	# else:
	#     raise Http404





def list_view(request):
	# list of items
	print(request)

	queryset = Product.objects.all()
	template = "list_view.html"
	context = {
		"queryset": queryset
	}
	return render(request, template, context)




