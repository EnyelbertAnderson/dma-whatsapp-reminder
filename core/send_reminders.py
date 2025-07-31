# core/management/commands/send_reminders.py
from django.core.management.base import BaseCommand
from core.whatsapp_sender import send_whatsapp
import datetime
import pymysql

class Command(BaseCommand):
    help = 'Enviar recordatorios de vencimiento por WhatsApp'

    def handle(self, *args, **kwargs):
        conn = pymysql.connect(host='localhost', user='root', password='tu_password', database='radius')
        cursor = conn.cursor()

        hoy = datetime.date.today().strftime('%Y-%m-%d')
        query = "SELECT username, phone FROM radcheck WHERE expiry = %s"
        cursor.execute(query, (hoy,))
        clientes = cursor.fetchall()

        for cliente in clientes:
            username, phone = cliente
            message = f"Hola {username}, tu servicio vence hoy. Por favor realiza tu pago para evitar la suspensión."
            send_whatsapp(phone, message)

        cursor.close()
        conn.close()
