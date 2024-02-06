from telegram.ext import Updater, CommandHandler
from django.core.management.base import BaseCommand
from myapp.models import Producto  # Asegúrate de cambiar 'miapp' por el nombre de tu aplicación

class Command(BaseCommand):
    help = "Telegram bot"

    def handle(self, *args, **options):
        updater = Updater(token='1931358215:AAHvnqdnP_rqAaNfcvhHg09UIUXKLkfLj2A', use_context=True)
        dp = updater.dispatcher

        dp.add_handler(CommandHandler("start", self.start))
        dp.add_handler(CommandHandler("productos", self.productos))

        updater.start_polling()
        updater.idle()

    def start(self, update, context):
        update.message.reply_text('Hola! Escribe /productos para ver la lista de productos.')

    def productos(self, update, context):
        productos = Producto.objects.all()
        message = ""
        for producto in productos:
            message += f"{producto.nombre} - {producto.precio}\n"
        update.message.reply_text(message)
