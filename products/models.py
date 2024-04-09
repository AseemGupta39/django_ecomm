from django.db.models import CharField
from django.db.models import ImageField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import TextField
from django.db.models import SlugField
from django.db.models import CASCADE

# Create your models here.
from base.models import BaseModel

class Category(BaseModel):
    category = CharField(max_length=100)
    slug = SlugField(unique=True,null=True,blank=True)
    category_image = ImageField(upload_to='categories')
    

class Product(BaseModel):
    product_name = CharField(max_length=100)
    slug = SlugField(unique=True,null=True,blank=True)
    category = ForeignKey(Category,on_delete=CASCADE,related_name="products")
    price = IntegerField()
    product_description = TextField()

class ProductImage(BaseModel):
    product = ForeignKey(Product,on_delete=CASCADE,related_name="product_images")
    image = ImageField(upload_to="product")


