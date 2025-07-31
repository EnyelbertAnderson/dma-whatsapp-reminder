from django.core.management.base import BaseCommand
from core.tasks import verificar_y_enviar_mensajes

class Command(BaseCommand):
    help = 'Envía recordatorios por WhatsApp según la fecha de vencimiento'

    def handle(self, *args, **kwargs):
        verificar_y_enviar_mensajes()
