class User():

    def __init__(self,first_name, last_name, age, eye_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.eye_color = eye_color


    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}, {self.age}, {self.eye_color}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

new_user = User('John', 'Doe', 21, 'Brown')
new_user2 = User('Mike', 'Doe', 27, 'Blue')
new_user3 = User('Lola', 'Doe', 29, 'Green')
new_user4 = User('Kevin', 'Doe', 13, 'Grey')

new_user.describe_user()
new_user.greet_user()
new_user2.describe_user()
new_user2.greet_user()
new_user3.describe_user()
new_user3.greet_user()
new_user4.describe_user()
new_user4.greet_user()
