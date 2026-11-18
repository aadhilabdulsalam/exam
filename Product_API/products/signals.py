from django.dispatch import receiver
from products.models import Product
from django.db.models.signals import post_delete

@receiver(post_delete, sender=Product)
def show_message(sender, instance, **kwargs):
    print("Product is deleted")
