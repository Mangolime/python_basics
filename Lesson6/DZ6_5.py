class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self):
        super().__init__('Ручка')

    def draw(self):
        print(f"Отрисовка с помощью инструмента {self.title}")


class Pencil(Stationery):

    def __init__(self):
        super().__init__('Карандаш')

    def draw(self):
        print(f"Отрисовка с помощью инструмента {self.title}")


class Handle(Stationery):

    def __init__(self):
        super().__init__('Маркер')

    def draw(self):
        print(f"Отрисовка с помощью инструмента {self.title}")


stat = Stationery("ластик")
pen = Pen()
pencil = Pencil()
handle = Handle()
stat.draw()
pen.draw()
pencil.draw()
handle.draw()
