from django.contrib import admin

from .models import Cargo, Servico, Funcionario, Adireita, Aesquerda


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icone', 'ativo', 'modificado')


@admin.register(Funcionario)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')


@admin.register(Adireita)
class AdireitaAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'icone', 'descricao', 'modificado')


@admin.register(Aesquerda)
class AesquerdaAdmin(admin.ModelAdmin):
    list_display = ('recurso', 'icone', 'descricao', 'modificado')

