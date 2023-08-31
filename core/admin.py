from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente

class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

admin.site.register(Produto, ProdutosAdmin)
admin.site.register(Cliente, ClienteAdmin)