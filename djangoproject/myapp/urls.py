from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # paginapordefecto
    path('', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('user-logout', views.user_logout, name="user-logout"),
    # Menu_Principal
    path('menuvista/', views.menuvista, name='menuvista'),

    # Proveedor
    path('agregar_proveedor/', views.agregar_proveedor, name='agregar_proveedor'),
    path('mostrar_proveedor/<str:ruc_proveedor>/',
         views.mostrar_proveedor, name='mostrar_proveedor'),
    path('editar_proveedor/<str:ruc_proveedor>/',
         views.editar_proveedor, name='editar_proveedor'),
    path('eliminar_proveedor/<str:ruc_proveedor>/',
         views.eliminar_proveedor, name='eliminar_proveedor'),
    path('list_proveedor/', views.list_proveedor, name='list_proveedor'),
    path('proveedores/', views.proveedores, name='proveedores'),

    # Ventas
    path('ventas/', views.ventas, name='ventas'),
    # Cliente
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('eliminar_cliente/<str:identificacion>/',
         views.eliminar_cliente, name='eliminar_cliente'),
    path('mostrar_cliente/<str:identificacion>/',
         views.mostrar_cliente, name='mostrar_cliente'),
    path('list_cliente/', views.list_cliente, name='list_cliente'),
    path('editar_cliente/<str:identificacion>/',
         views.editar_cliente, name='editar_cliente'),
    path('clientes/', views.clientes, name='clientes'),
    path('buscar_cliente/<str:identificacion>/',
         views.buscar_cliente, name='buscar_cliente'),
    # Producto
    path('productos/', views.productos, name='productos'),
    path('eliminar_producto/<str:codigo_producto>/',
         views.eliminar_producto, name='eliminar_producto'),
    path('mostrar_producto/<str:codigo_producto>/',
         views.mostrar_producto, name='mostrar_producto'),
    path('editar_producto/<str:codigo_producto>/',
         views.editar_producto, name='editar_producto'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('list_producto/', views.list_producto, name='list_producto'),
    path('buscar_producto/<str:codigo>/',
         views.buscar_producto, name='buscar_producto'),
    # UsuarioSistema
    path('crearusuario/', views.create_profile, name='create_profile'),
    path('list_profile/', views.list_profile, name='list_profile'),
    path('profile/', views.profile, name='profile'),
    path('editarprofile/', views.editarprofile, name='editarprofile'),
    path('mostrarprofile/<str:cedula>/', views.mostrar_profile, name='mostrarprofile'),
    #reportes
    path('reportes/', views.reportes, name='reportes'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
