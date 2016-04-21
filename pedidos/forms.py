from django import forms
from .models import Pedido
from django.forms import ModelForm, DateField
from datetime import datetime

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class PedidoForm(ModelForm):
    fecha_entrega_pedido= forms.DateField(help_text="dia/mes/año",initial=datetime.now, widget=forms.DateInput(format='%d/%m/%Y'),input_formats=('%d/%m/%Y',))
    #fecha_entrega_pedido = forms.DateField(required=True, help_text="dia/mes/año",initial=datetime.now)
    hora_entrega_pedido= forms.TimeField(help_text="Hora:minuto",widget=forms.TimeInput(format='%H:%M'),input_formats=('%H:%M',))

    class Meta:
        model=Pedido
        fields = ('identificador_pedido','numero_guiavm','numero_guia','nombre_cliente',
                  'descripcion_corta_pedido','descripcion_larga_pedido','deseo_borrar',
                  'estado_pedido','fecha_entrega_pedido','hora_entrega_pedido','direccion_entrega_pedido',
                  'sucursal_entrega_pedido','abono_pedido','precio_total_pedido','metodo_pago_pedido','celular_cliente',
                  'telefono_cliente','correo_cliente')
        widgets = {
            'numero_guiavm': forms.TextInput(
                attrs={'placeholder': 'Ingrese el número de la guia de Vicuña mackenna'}),
            'numero_guia': forms.TextInput(
                attrs={'placeholder': 'Ingrese el número de la guia de este local'}),
            'identificador_pedido': forms.TextInput(attrs={'placeholder': 'Ingrese un texto para identificar su pedido'}),

            #'fecha_entrega_pedido': forms.DateInput(format=('%d-%m-%Y'),    attrs={'style': 'width:10px'}
                                         #    attrs={'placeholder': 'Select a date'})

        }



