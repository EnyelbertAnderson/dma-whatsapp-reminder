from datetime import datetime, timedelta
from .models import RmUsers
from .selenium_bot import enviar_mensaje
import os

def verificar_y_enviar_mensajes():
    hoy = datetime.now().date()
    mañana = hoy + timedelta(days=1)

    usuarios = RmUsers.objects.filter(expiration__in=[hoy, mañana])
    for usuario in usuarios:
        nombre = usuario.username
        numero = usuario.mobile
        fecha = usuario.expiration.strftime('%d/%m/%Y')
        mensaje = os.getenv("WHATSAPP_MENSAJE").format(nombre=nombre, fecha=fecha)
        if numero:
            enviar_mensaje(numero, mensaje)
