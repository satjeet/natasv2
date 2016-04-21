from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Pedido(models.Model):
    opciones_estados_pedidos=(
        ('PAGADO','Pagado'),('PENDIENTE','Pago Pendiente'),
        ('RESERVADO','Reservado'),('DESPACHABLE','Listo para despachar'),('ENTREGABLE','Listo para entregar')
    )
    opciones_sucursales=(
        ('VICUNA','Vicuna Mackenna'),('MIRADOR','Mirador Azul'),('TOBALABA','Tobalaba'),('DOMICILIO','Domicilio')
    )
    opciones_metodos_pago=(
        ('TRANSFERENCIA','Transferencia electronica'),('EFECTIVO','Efectivo'),
        ('CHEQUE','Cheque'),('CREDITO','Tarjeta de Credito'),('OTRO','Otro metodo')
    )
    #numero_guiavm=models.CharField('numero de guia de vicuña'.max_length=50,blank=True)
    identificador_pedido=models.CharField(max_length=50,blank=True)
    numero_guiavm=models.CharField(max_length=50,blank=True)
    numero_guia = models.CharField(max_length=50)
    nombre_cliente = models.CharField(max_length=100)
    descripcion_corta_pedido= models.CharField(max_length=100,blank=True)
    descripcion_larga_pedido = models.TextField()
    vendedor= models.ForeignKey('auth.User')
    deseo_borrar=models.BooleanField(default=False)
    estado_pedido= models.CharField(max_length=50,choices=opciones_estados_pedidos,default='PENDIENTE')
    fecha_entrega_pedido=models.DateField()
    hora_entrega_pedido=models.TimeField()
    direccion_entrega_pedido=models.CharField(max_length=150,blank=True)
    sucursal_entrega_pedido=models.CharField(max_length=50,choices=opciones_sucursales,default='VICUNA')
    abono_pedido=models.CharField(max_length=12)
    precio_total_pedido=models.CharField(max_length=12)
    metodo_pago_pedido=models.CharField(max_length=50,choices=opciones_metodos_pago,default='TRANSFERENCIA')
    celular_cliente=models.CharField(max_length=12,blank=True)
    telefono_cliente=models.CharField(max_length=12,blank=True)
    correo_cliente=models.EmailField(blank=True)
    fecha_creacion_pedido=models.DateTimeField(auto_now_add=True,auto_now=False)

    def __str__(self):
        return self.nombre_cliente