import os
import django
from django.contrib.auth.models import User

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeServiceManagement.settings')
django.setup()

from home_service.models import Status, Customer, Service_Man, City

def seed():
    print("Starting data seeding...")
    
    # Create Statuses
    statuses = ['pending', 'Accept', 'unread']
    for s in statuses:
        Status.objects.get_or_create(status=s)
    
    # Create Cities
    City.objects.get_or_create(city="New York")
    City.objects.get_or_create(city="Mumbai")
    
    # Admin
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Admin created.")
    
    # User
    if not User.objects.filter(username='user').exists():
        user_obj = User.objects.create_user('user', 'user@example.com', 'user')
        user_obj.first_name = "Demo"
        user_obj.last_name = "User"
        user_obj.save()
        Customer.objects.create(user=user_obj, contact="1234567890", address="Test Address")
        print("User created.")
    
    # Service Provider
    if not User.objects.filter(username='serviceprovider').exists():
        sp_obj = User.objects.create_user('serviceprovider', 'sp@example.com', 'serviceprovider')
        sp_obj.first_name = "Demo"
        sp_obj.last_name = "Provider"
        sp_obj.save()
        status_accept = Status.objects.get(status='Accept')
        city_obj = City.objects.first()
        Service_Man.objects.create(
            user=sp_obj, 
            contact="9876543210", 
            address="Service Address", 
            status=status_accept,
            city=city_obj,
            service_name="Cleaning",
            experience="5 years"
        )
        print("Service Provider created.")

if __name__ == "__main__":
    seed()
