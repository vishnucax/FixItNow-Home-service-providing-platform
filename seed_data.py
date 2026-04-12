import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeServiceManagement.settings')
django.setup()

from django.contrib.auth.models import User
from home_service.models import Status, Customer, Service_Man, City

def seed():
              if not User.objects.filter(username='admin').exists():
                              User.objects.create_superuser('admin', 'admin@example.com', 'admin')
                            if not User.objects.filter(username='serviceprovider').exists():
                                            user = User.objects.create_user('serviceprovider', 'sp@example.com', 'serviceprovider')
                                            Service_Man.objects.get_or_create(user=user, name='SP', contact='1', address='A', id_card='I')
                                          if not User.objects.filter(username='user').exists():
                                                          user = User.objects.create_user('user', 'user@example.com', 'user')
                                                          Customer.objects.get_or_create(user=user, name='U', contact='2', address='B')

if __name__ == "__main__":
              seed()
