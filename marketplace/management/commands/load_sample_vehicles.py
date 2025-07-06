# marketplace/management/commands/load_sample_vehicles.py

from django.core.management.base import BaseCommand
from marketplace.models import Vehicle

class Command(BaseCommand):
    help = 'Load sample vehicles into the database'

    def handle(self, *args, **kwargs):
        # Cars
        Vehicle.objects.create(title='Honda Civic 2022', vehicle_type='car', description='A reliable sedan with modern features.', price=21000, image='vehicles/civic.jpg')
        Vehicle.objects.create(title='Hyundai Creta SX 2023', vehicle_type='car', description='Stylish compact SUV with sunroof.', price=24500, image='vehicles/creta.jpg')
        Vehicle.objects.create(title='Tata Nexon EV Max', vehicle_type='car', description='Electric SUV with 400+ km range.', price=29000, image='vehicles/nexon_ev.jpg')
        Vehicle.objects.create(title='Toyota Fortuner', vehicle_type='car', description='Powerful 7-seater with off-road capabilities.', price=45000, image='vehicles/fortuner.jpg')
        Vehicle.objects.create(title='Maruti Suzuki Swift', vehicle_type='car', description='Compact and efficient hatchback.', price=12000, image='vehicles/swift.jpg')

        # Bikes
        Vehicle.objects.create(title='Royal Enfield Classic 350', vehicle_type='bike', description='Retro design with modern tech.', price=5000, image='vehicles/classic350.jpg')
        Vehicle.objects.create(title='Yamaha R15 V4', vehicle_type='bike', description='Sporty design and powerful 155cc engine.', price=3200, image='vehicles/r15.jpg')
        Vehicle.objects.create(title='KTM Duke 250', vehicle_type='bike', description='Aggressive streetfighter with quick pickup.', price=4000, image='vehicles/duke250.jpg')
        Vehicle.objects.create(title='TVS Apache RR 310', vehicle_type='bike', description='Fully faired bike with racing DNA.', price=4800, image='vehicles/apache_rr.jpg')
        Vehicle.objects.create(title='Hero Splendor Plus', vehicle_type='bike', description='Best-selling commuter bike in India.', price=1200, image='vehicles/splendor.jpg')

        self.stdout.write(self.style.SUCCESS("Sample vehicles added."))