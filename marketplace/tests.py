# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Vehicle, CartItem, Cart

# class VehicleModelTest(TestCase):
#     def test_vehicle_creation(self):
#         vehicle = Vehicle.objects.create(
#             title='Test Car',
#             vehicle_type='car',
#             brand='Toyota',
#             model_name='Corolla',
#             description='A reliable car',
#             price=20000.00,
#             fuel_type='Petrol',
#             mileage=15000
#         )
#         self.assertEqual(vehicle.title, 'Test Car')
#         self.assertEqual(vehicle.brand, 'Toyota')
#         self.assertEqual(vehicle.vehicle_type, 'car')
#         self.assertEqual(vehicle.mileage, 15000)

# class CartItemModelTest(TestCase):
#     def test_cart_item_creation(self):
#         user = User.objects.create_user(username='testuser', password='testpass')
#         vehicle = Vehicle.objects.create(
#             title='Test Bike',
#             vehicle_type='bike',
#             brand='Yamaha',
#             model_name='FZ',
#             description='A sporty bike',
#             price=1500.00,
#             fuel_type='Petrol',
#             mileage=2000
#         )
#         cart_item = CartItem.objects.create(
#             user=user,
#             vehicle=vehicle,
#             quantity=2
#         )
#         self.assertEqual(cart_item.user.username, 'testuser')
#         self.assertEqual(cart_item.quantity, 2)
#         self.assertEqual(cart_item.vehicle.title, 'Test Bike')

# class CartModelTest(TestCase):
#     def test_cart_creation(self):
#         user = User.objects.create_user(username='testuser', password='testpass')
#         cart = Cart.objects.create(user=user)
#         self.assertEqual(cart.user.username, 'testuser')
#         self.assertIsInstance(cart.created_at, str)  # Checking if 'created_at' is a valid date string
