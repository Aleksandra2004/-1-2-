# TODO Написать 3 класса с документацией и аннотацией типов

class AbstractObject:
    def init(self, name: str, color: str):

        """
    Constructor for AbstractObject class.
        :param name: A string representing the name of the object.
        :param color: A string representing the color of the object.
        """


self.name = name
self.color = color

def move(self, direction: str):
    """
   Переместите объект в заданном направлении.

    :param direction: A string representing the direction to move the object.
    :return: A message confirming the movement of the object.

    >>> obj = AbstractObject("obj1", "red")
    >>> obj.move("up")
    "Объект obj1 переместился вверх".
    """

def change_color(self, new_color: str):
    """
    Измените цвет объекта.

    :param new_color: A string representing the new color of the object.
    :return: A message confirming the color change.

    >>> obj = AbstractObject("obj2", "blue")
    >>> obj.change_color("green")
    "Цвет объекта obj2 изменен на зеленый".
    """


def interact(self):
    """
Выполните взаимодействие с объектом.

    :return: A message describing the interaction.

    >>> obj = AbstractObject("obj3", "yellow")
    >>> obj.interact()
    "Объект, с которым взаимодействовал obj3".
    """

    class Tree(AbstractObject):
        def init(self, name: str, color: str, age: int):

            """
        Constructor for Tree class.
            :param name: A string representing the name of the tree.
            :param color: A string representing the color of the tree.
            :param age: An integer representing the age of the tree.
            """

    super().__init__(name, color)
    self.age = age


def grow(self, years: int):
    """
Смоделируйте рост дерева в течение заданного количества лет.

    :param years: An integer representing the number of years for the tree to grow.
    :return: A message indicating the growth of the tree.

    >>> tree = Tree("oak", "green", 10)
    >>> tree.grow(5)
    "Дерево дуб росло 5 лет".
    """


class Car(AbstractObject):
    def init(self, name: str, color: str, brand: str):

        """
    Constructor for Car class.
        :param name: A string representing the name of the car.
        :param color: A string representing the color of the car.
        :param brand: A string representing the brand of the car.
        """


super().__init__(name, color)
self.brand = brand


def drive(self, distance: float):
    """
    Имитируйте движение автомобиля на заданное расстояние.

    :param distance: A float representing the distance in kilometers to drive.
    :return: A message indicating the distance driven.

    >>> car = Car("sedan", "silver", "Toyota")
    >>> car.drive(50.5)
    "Автомобиль седан проехал 50,5 км."
    """


def honk(self):
    """
    Produce a honking sound from the car horn.

    :return: A message indicating the car horn has honked.

    >>> car = Car("SUV", "black", "Ford")
    >>> car.honk()
    "Автомобиль-внедорожник просигналил клаксоном".
    """