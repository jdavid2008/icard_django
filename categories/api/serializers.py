from rest_framework.serializers import ModelSerializer
from categories.models import Category

class CategorySerializar(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title','image']