class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.name} {self.speed} км/ч')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость машины {self.name} {self.speed} км/ч')
        else:
            print('Превышение скорости')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость машины {self.name} {self.speed} км/ч')
        else:
            print('Превышение скорости')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


sport = SportCar(140, 'красная', 'BMW')
sport.go()
sport.turn('направо')
sport.show_speed()
work = WorkCar(50, 'оранжевый', 'трактор')
work.go()
work.show_speed()
police = PoliceCar(100, 'синяя', 'Hyundai')
police.go()
print(police.is_police)
print(police.color)