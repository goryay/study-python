class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This restaurant has name is {self.restaurant_name}")
        print(f'The cuisine of this restaurant {self.cuisine_type}')

    def open_restaurant(self):
        print(f"This restaurant is {self.restaurant_name} open")

restaurant_info = Restaurant("Chicken", 'mexico')
restaurant_info.describe_restaurant()
restaurant_info.open_restaurant()

more_restaurant_info = Restaurant("KFC", 'usa')
more_restaurant_info.describe_restaurant()
more_restaurant_info.open_restaurant()

one_more_restaurant = Restaurant("Tokyo", 'chinese')
one_more_restaurant.describe_restaurant()
one_more_restaurant.open_restaurant()
