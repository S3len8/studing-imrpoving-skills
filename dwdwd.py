class Home():
    default_wall_material = "Кирпич"

    def __init__(self, color, floors, sec_code):
        self.color = color # Public attribute
        self._floors = floors # Secure attribute
        self.__sec_code = sec_code # Private attribute

    def describe(self):
        print(f"House: {self.color}, Floors: {self._floors}, Sec Code: {self.__sec_code}")

    def repaint(self, new_color):
        self.color = new_color
        print(f"Paint house: {self.color}")


h1 = Home("White", 15, 893123)
# h2 = Home("Orange", 11, 1231311)

print(h1.color)
print(h1._floors)
print(h1.__sec_code)