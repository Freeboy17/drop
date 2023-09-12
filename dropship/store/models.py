from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, related_name = 'customer', on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)


    class Meta:

        verbose_name_plural = 'categories'


    def __str__(self):

        return self.name


    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])



class Product(models.Model):

    #FK 

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)


    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    image = models.ImageField(upload_to='images/')


    class Meta:

        verbose_name_plural = 'products'


    def __str__(self):

        return self.title



    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)
	
class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address

	
