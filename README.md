# DMA WhatsApp Reminder

Sistema que detecta usuarios por vencer en DMA Radius Manager y les envía un mensaje por WhatsApp con Selenium.

## Instalación

```bash
git clone https://github.com/enypanta/dma-whatsapp-reminder.git
cd dma-whatsapp-reminder
python3.8 -m venv env
source env/bin/activate
pip install -r requirements.txt
cp .env.example .env
nano .env  # Configura tu base de datos
python manage.py send_reminders
```

## Requisitos

- CentOS 7
- Python 3.8
- Django
- Selenium
- Chromium y ChromeDriver
