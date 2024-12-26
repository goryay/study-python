class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"This restaurant has name is {self.restaurant_name}")
        print(f'The cuisine of this restaurant {self.cuisine_type}')

    def open_restaurant(self):
        print(f"This restaurant is {self.restaurant_name} open")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print(f"This restaurant is {self.restaurant_name} set {number_served}")

    def increment_number_served(self, number_served):
        self.number_served += number_served
        print(f"The restaurant {self.restaurant_name} served an additional {number_served} customers.")
        print(f"Total customers served: {self.number_served}.")


# restaurant_info = Restaurant("Chicken", "Mexican")
#
# print(f"Default number served: {restaurant_info.number_served}")
#
# restaurant_info.set_number_served(100)
# print(f"Updated number served: {restaurant_info.number_served}")
#
# restaurant_info.increment_number_served(400)


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavour = []

    def show_flavour(self):
        if self.flavour:
            print(f"This restaurant is {self.restaurant_name}")
            for flavour in self.flavour:
                print(flavour)
        else:
            print("This restaurant is empty")

# ice_cream_list = IceCreamStand("Sweet Treats", "Ice Cream")
# ice_cream_list.flavour = ["Vanilla", "Chocolate", "Strawberry", "Mint"]
#
# ice_cream_list.describe_restaurant()
# ice_cream_list.show_flavour()