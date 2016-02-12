from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.urlresolvers import reverse
from django.utils.text import slugify


# Create your models here.



def download_mdedia_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="managers_product", blank=True)
    title = models.CharField(max_length=140)  # sdlfldsfjaslk
    media = models.FileField(blank=True,
                             null=True,
                             upload_to=download_mdedia_location,
                             storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
    slug = models.SlugField(blank=True, unique=True)#unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=9.99)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, default=6.99, blank=True, null=True)




    def __str__(self):
        return self.title

    def get_absolute_url(self):
        viewname = "product_detail_slug_view"
        return reverse(viewname, kwargs={"slug": self.slug})

    def get_download(self):
        view_name = "products:download_slug"

class Thumbnail(models.Model):
    product = models.ForeignKey(Product)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    height = models.CharField(max_length=20, null=True, blank=True)
    width = models.CharField(max_length=20, null=True, blank=True)
    media = models.ImageField(
                            width_field= "width",
                            height_field= "height",
                            blank=True,
                            null=True,
                            uplod_to=download_mdedia_location
    )

    def __str__(self):
        return str(self.media.path)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug

    qs = Product.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        print(instance.slug)

        # instance.slug = slugify(instance.title)

pre_save.connect(product_pre_save_reciever, sender=Product)


# def product_post_save_reciever(sender, instance, *args, **kwargs):
#     if instance.slug != slugify(instance.title):
#         instance.slug = slugify(instance.title)
#         instance.save()
#
# post_save.connect(product_post_save_reciever, sender=Product)
