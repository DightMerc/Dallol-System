import os, sys

# from django.core.wsgi import get_wsgi_application
# from django.contrib.auth.models import User
# from django.utils import timezone
import django
# from django.conf import settings
 



proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0] + "\\bothelper\\"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bothelper.settings")
sys.path.append(proj_path)

django.setup()

from api import models as api_models
from bot import models as bot_models




def getMessage(number):
    return bot_models.Message.objects.get(number=number)

def getRegions():
    return bot_models.Region.objects.all()

def userExsists(user):
    try:
        api_models.TelegramUser.objects.get(telegram_id=int(user))
        return True
    except Exception as identifier:
        return False

def userCreate(user):
    new_user = api_models.TelegramUser()

    new_user.telegram_id = user.id
    new_user.full_name = user.full_name
    new_user.username = user.username

    new_user.save()

    return True

def getUser(user):
    try:
        api_models.TelegramUser.objects.get(telegram_id=int(user))
        return api_models.TelegramUser.objects.get(telegram_id=int(user))
    except Exception as identifier:
        return False


def userSetLanguage(user, language):
    
    current_user = api_models.TelegramUser.objects.get(telegram_id=int(user))
    current_user.language = language

    current_user.save()
