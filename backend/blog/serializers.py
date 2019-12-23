#backend/blog/serializers.py
from rest_framework import serializers
from .models import Blog,Menu,Category

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Blog

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Menu
 
class RecursiveField(serializers.BaseSerializer):
    """
    Cria instancia do serializer parente e retorna os dados
    serializados.
    """
    def to_representation(self, value):
        ParentSerializer = self.parent.parent.__class__
        serializer = ParentSerializer(value, context=self.context)
        return serializer.data
    def to_internal_value(self, data):
        ParentSerializer = self.parent.parent.__class__
        Model = ParentSerializer.Meta.model
        try:
            instance = Model.objects.get(pk=data)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                "Objeto {0} não encontrado".format(
                    Model().__class__.__name__
                )
            )
        return instance
class CategorySerializer(serializers.ModelSerializer):
    subcategories = RecursiveField(source="children",
                                   many=True, required=False)
    class Meta:
        model = Category
        fields = ("id", "name", "level", "link", "slug", "parent", "subcategories",)
