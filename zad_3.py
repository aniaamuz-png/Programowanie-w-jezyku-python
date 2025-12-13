class Property:
    def __init__(self, area, rooms: int, price: float, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
    def __str__(self):
        return f'Property has {self.area} area, {self.rooms} rooms and costs {self.price} dollars.'
class House(Property):
    def __init__(self, area, rooms, price, address,plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    def __str__(self):
        return f'House has {self.plot} square meters'
class Flat(Property):
    def __init__(self, area, rooms, price, address, floor: str):
        super().__init__(area, rooms, price, address)
        self.floor = floor
    def __str__(self):
        return f'Flat is located on the {self.floor} floor'

house = House(120, 5, 350000, "Main Street 10", 500)
flat = Flat(60, 3, 220000, "Green Avenue 5/12", 3)

print(house)
print(flat)