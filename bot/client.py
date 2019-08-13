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
