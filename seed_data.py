import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeServiceManagement.settings'); django.setup()
from django.contrib.auth.models import User
from home_service.models import *
try: User.objects.create_superuser('admin', 'a@a.com', 'admin')
      except: pass
            try:
                   u1 = User.objects.create_user('serviceprovider', 's@s.com', 'serviceprovider')
                   Service_Man.objects.create(user=u1, name='S', contact='1', address='A', id_card='I')
                  except: pass
                        try:
                               u2 = User.objects.create_user('user', 'u@u.com', 'user')
                               Customer.objects.create(user=u2, name='U', contact='2', address='B')
                              except: pass
                                    
