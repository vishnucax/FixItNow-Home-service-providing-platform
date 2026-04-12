import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeServiceManagement.settings')
django.setup()
from django.contrib.auth.models import User
from home_service.models import *
def seed():
      if not User.objects.filter(username='admin').exists():
              User.objects.create_superuser('admin', 'a@a.com', 'admin')
            if not User.objects.filter(username='serviceprovider').exists():
                    u = User.objects.create_user('serviceprovider', 's@s.com', 'serviceprovider')
                    Service_Man.objects.create(user=u, name='S', contact='1', address='A', id_card='I')
                  if not User.objects.filter(username='user').exists():
                          u = User.objects.create_user('user', 'u@u.com', 'user')
                          Customer.objects.create(user=u, name='U', contact='2', address='B')
                      if __name__ == "__main__":
                            seed()
                          
