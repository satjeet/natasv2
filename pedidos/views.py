from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Pedido
from datetime import datetime, timedelta
from django.contrib.auth import authenticate, login
from .forms import LoginForm, PedidoForm
from django.contrib.auth.decorators import permission_required


# Create your views here.

def pedido_detalle(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedidos/pedido_detalle.html', {'pedido': pedido})

def index(request):
    pedidos=Pedido.objects.order_by('fecha_entrega_pedido')
    return render(request, 'pedidos/index.html',{'pedidos': pedidos})
    #return HttpResponse(" Bienvenido al index de la pagina")

def pedidos_semana(request):
    una_semana = datetime.today() + timedelta(days=7)
    pedidos = Pedido.objects.filter(fecha_entrega_pedido__lte=una_semana).order_by('fecha_entrega_pedido')
    return render(request, 'pedidos/unasemana.html', {'pedidos': pedidos})
    # return HttpResponse(" Bienvenido al index de la pagina")

def pedidos_hoy(request):
    una_semana = datetime.today()
    pedidos = Pedido.objects.filter(fecha_entrega_pedido__lte=una_semana).order_by('fecha_entrega_pedido')
    return render(request, 'pedidos/parahoy.html', {'pedidos': pedidos})
    # return HttpResponse(" Bienvenido al index de la pagina")


def pedidos_tresdias(request):
    una_semana = datetime.today() + timedelta(days=3)
    pedidos = Pedido.objects.filter(fecha_entrega_pedido__lte=una_semana).order_by('fecha_entrega_pedido')
    return render(request, 'pedidos/tresdias.html', {'pedidos': pedidos})
    # return HttpResponse(" Bienvenido al index de la pagina")

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid Login')
    else:
        form=LoginForm()
    return render(request,'account/login.html',{'form':form})

def pedido_new(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.vendedor = request.user
            pedido.fecha_creacion_pedido = datetime.now()
            pedido.save()
            return redirect('pedido_detalle', pk=pedido.pk)
    else:
        form = PedidoForm()
    return render(request, 'registration/pedido_edit.html',{'form':form})

@permission_required('pedidos.can_edit',login_url='index')
def pedido_edit(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.author = request.user
            pedido.published_date = datetime.now()
            pedido.save()
            return redirect('pedido_detalle', pk=pedido.pk)
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'registration/pedido_edit.html', {'form': form})