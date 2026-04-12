import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeServiceManagement.settings')
django.setup()
from django.contrib.auth.models import User
from home_service.models import Status, Customer, Service_Man, City
def seed():
    if not User.objects.filter(username="admin").exists():
          User.objects.create_superuser("admin", "admin@example.com", "admin")
    f not User.objects.filter(username="serviceprovider").exists():
              u = User.objects.create_user("serviceprovider", "sp@example.com", "serviceprovider")
              Service_Man.objects.create(user=u, name="SP", contact="1", address="A", id_card="I")
        f not User.objects.filter(username="user").exists():
                  u = User.objects.create_user("user", "u@example.com", "user")
                  Customer.objects.create(user=u, name="U", contact="2", address="B")
    f __name__ == "__main__":
                  seed()
                
