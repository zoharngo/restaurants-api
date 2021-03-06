from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import RestaurantModel

url = reverse('restaurantmodel-list')

def createRestaurant(client):   
    data = [{'restaurant_name' : 'Hudson',
             'restaurant_type' : 'Grill',
             'phone' : '+(972) 3644 4733',
             'location': {
			    'coordinates': '32.109805/34.840232',
			    'address': ''}
            }]
    return client.post(url, data, format='json')

class TestCreateRestaurant(APITestCase):
    """
        Enusre we can create a new restaurant
    """
    def setUp(self):
        self.response = createRestaurant(self.client)

    def test_received_201_created_status_code(self):   
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_restaurant_was_created(self):
        self.assertEqual(RestaurantModel.objects.count(), 1)

    def test_restaurant_has_correct_name(self):
        self.assertEqual(RestaurantModel.objects.get().restaurant_name, 'Hudson')

class TestsUpdateRestaurant(APITestCase):
    """
        Ensure we can update an existing restaurant using PUT
    """

    def setUp(self):
        createRestaurant(self.client)
        self.assertEqual(RestaurantModel.objects.get().restaurant_name, 'Hudson')
        data = {'restaurant_name': 'Humongous', 'restaurant_type': 'Burger'}
        self.response = self.client.put("/".join([url,RestaurantModel.objects.get().uuid]), data, format='json')
    
    def test_received_200_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_restaurant_was_updated(self):
        self.assertEqual(RestaurantModel.objects.get().restaurant_type, 'Burger')

class TestsPatchRestaurant(APITestCase):
    """
        Ensure we can update an existing restaurant using PATCH
    """

    def setUp(self):
        createRestaurant(self.client)
        self.assertEqual(RestaurantModel.objects.get().restaurant_name, 'Hudson')
        data = {'restaurant_name': 'Humongous', 'phone': "(+972) 050 - 4945555" }
        self.response = self.client.patch("/".join([url,RestaurantModel.objects.get().uuid]), data, format='json')
    
    def test_received_200_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_restaurant_was_updated(self):
        self.assertEqual(RestaurantModel.objects.get().restaurant_name, 'Humongous')
        self.assertEqual(RestaurantModel.objects.get().phone, "(+972) 050 - 4945555")

class TestsDeleteRestaurantItem(APITestCase):
    """
        Enusre we can delete a api item
    """

    def setUp(self):
        createRestaurant(self.client)
        self.assertEqual(RestaurantModel.objects.count(), 1)
        self.response = self.client.delete("/".join([url,RestaurantModel.objects.get().uuid]))

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_the_restaurant_was_deleted(self):
        self.assertEqual(RestaurantModel.objects.count(), 0)


class TestsDeleteAllRestaurants(APITestCase):
    """
        Ensure we can delete all items
    
    """

    def setUp(self):
        createRestaurant(self.client)
        self.assertEqual(RestaurantModel.objects.count(), 1)
        self.response = self.client.delete(reverse('restaurantmodel-list'))

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_all_restaurants_were_deleted(self):
        self.assertEqual(RestaurantModel.objects.count(), 0)





        
