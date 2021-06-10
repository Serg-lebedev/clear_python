class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    def descibe_restaurant(self):
        print(f'Имя ресторана: {self.restaurant_name} тип кухни: {self.cuisine_type} customers {self.number_served}')
    def open_restaurant(self):
        print(f'Ресторан открытый')
    def numbers_served(self, customers):
        self.number_served = customers
    def increment_number_served(self, inc):
        self.number_served += inc
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors='Cold_ice'
    def flavors_print(self):
        print(f'\n{self.flavors}')
adachi = Restaurant('Adachi', 'Chinese_food')
dacha = Restaurant('dacha', 'french food')
barberry = Restaurant('gavno', 'bad food')
restaurant = Restaurant("kayf", 'real kayf')
print(f'Trying class {restaurant.restaurant_name} and {restaurant.cuisine_type}')
barberry.numbers_served(5)
barberry.increment_number_served(6)
barberry.descibe_restaurant()
adachi.descibe_restaurant()
dacha.descibe_restaurant()
IceCreamStand = IceCreamStand('kacheli','icecream')
IceCreamStand.descibe_restaurant()
IceCreamStand.flavors = 'Plombir'
IceCreamStand.flavors_print()