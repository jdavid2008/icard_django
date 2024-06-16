from rest_framework.serializers import ModelSerializer
from products.models import Product

class ProductSerializar(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','image','price','category']