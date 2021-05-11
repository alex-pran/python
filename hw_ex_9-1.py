class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}, {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} open!!!")
        
    def set_number_served(self):
        print(f"In restaurant {self.restaurant_name} served {self.number_served}")

    def increment_number_served(self, people):
        self.number_served += people

# ниже экземпляры
new_rest = Restaurant('Meet', 'Russian', 20)
print(new_rest.set_number_served())

new_rest.increment_number_served(2)

rest1 = Restaurant('Meet', 'Russian')
rest2 = Restaurant('Sofi', 'mediterian')
rest3 = Restaurant('Tanoreen', 'Mediterian')
rest4 = Restaurant('Blue Agave', 'mexican')
rest1.describe_restaurant()
rest1.open_restaurant()

rest2.describe_restaurant()
rest3.describe_restaurant()
rest4.describe_restaurant()

print(f"{rest1.open_restaurant} open!!!")