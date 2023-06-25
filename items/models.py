from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

User = get_user_model()


class Product(models.Model):
    
    Categorie_CHOICES = (
    ("Café", "Café"),
    ("Cafféine", "Cafféine"),
    ("Suppléments", "Suppléments"),
    ("Espresso", "Espresso"),
    ("Pâtisseries", "Pâtisseries"),

    )
    image=models.ImageField(upload_to='photos/%y/%m/%d', default="photos/23/05/21/no-product-image.png")
    name=models.CharField(max_length=100)
    description=models.TextField(null=True,blank=True)
    price=models.DecimalField(max_digits=6, decimal_places=2)
    date_ajout=models.DateTimeField(auto_now_add=True)
    is_available=models.BooleanField(default=True)
    categorie=models.CharField(max_length=100, default="Pâtisseries",choices=Categorie_CHOICES)

    def __str__(self) :
        return self.name
    
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name="carts")
    products = models.ManyToManyField(Product,)
    is_paid=models.BooleanField(default=False)
    def __str__(self) :
        return str(self.user)
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    def __str__(self):
            return f"Product: {self.product.name} - Quantity: {self.quantity}"
        

