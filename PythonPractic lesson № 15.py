# ЗАДАНИЕ 1

# class Transport:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def vivod(self):
#         print(f'Название автомобиля: {self.name}, скорость: {self.max_speed}, пробег: {self.mileage}')
    
# autobus = Transport('Lada 2109', 180, 150)
# autobus.vivod()

# ЗАДАНИЕ 2

class Transport:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity
    def seating_capacity(self, capacity):
        return print(f'Вместимость одного автобуса {self.name} {capacity} пассажиров')


class Autobus(Transport):
    def __init__(self, name, max_speed, mileage, capacity=50):
        super().__init__(name, max_speed, mileage, capacity)
   

bus = Autobus('Икарус', 100, 150)
bus.seating_capacity(50)