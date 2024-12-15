class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def go_to(self, new_floor):
        floor = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            while floor <= new_floor:
                print(floor)
                floor += 1

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акция', 20)
print(h1) # __str__
print(h2) # __str__
print(len(h1)) # __len__
print(len(h2)) # __len__