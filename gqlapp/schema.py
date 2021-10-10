from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from gqlapp.models import Product
import graphene




class Products(DjangoObjectType):
    class Meta:
        model = Product
        filter_fields = ['id','segment', 'country', 'sales']
        interfaces = (relay.Node, )


        

class Query(graphene.ObjectType):
    product_info = relay.Node.Field(Products)
    all_product_info = DjangoFilterConnectionField(Products)

    def resolve_prodinfo(self, info):
        return Product.objects.all()


schema = graphene.Schema(query=Query)