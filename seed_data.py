import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeServiceManagement.settings')
django.setup()

from django.contrib.auth.models import User
from home_service.models import Status, Customer, Service_Man, City

def seed():
        print("Starting data seeding...")

    # Create Statuses
        statuses = ['pending', 'Accept', 'unread']
        for s in statuses:
                    Status.objects.get_or_create(status=s)

        # Create Admin
        if not User.objects.filter(username='admin').exists():
                    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
                    print("Admin user created.")

        # Create Service Provider
        if not User.objects.filter(username='serviceprovider').exists():
                    user = User.objects.create_user('serviceprovider', 'sp@example.com', 'serviceprovider')
                    Service_Man.objects.get_or_create(user=user, name='Service Provider', contact='1234567890', address='Service City', id_card='ID123')
                    print("Service provider created.")

        # Create User
        if not User.objects.filter(username='user').exists():
                    user = User.objects.create_user('user', 'user@example.com', 'user')
                    Customer.objects.get_or_create(user=user, name='Normal User', contact='0987654321', address='User City')
                    print("Normal user created.")

    if __name__ == "__main__":
            seed()
        
