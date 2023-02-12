if __name__ == "__main__":
    class Car:
        """Базовый класс"""

        def __init__(self, country: str, length: int, width: int, power: int, color: str):
            """
            метод-конструктор
            country -- страна производитель
            length -- длина, мм
            width -- высота, мм
            power -- power, л.с.
            color -- цвет
            """
            self.country = country
            self.length = length
            self.width = width
            self.power = power
            self.color = color

        def __str__(self):
            """метод, возвращающий стороку с страной-произодителем,длиной, шириной, мощностью и цветом авто"""
            return f'Cтрана производитель: {self.country}. Длина: {self.length}. Ширина: {self.width}. Мощность: {self.power}.' \
                   f' Цвет: {self.color}'

        def __repr__(self):
            """"метод, возвращающий валидную Python строку, точно такого же экзампляра"""
            return f'{self.__class__.__name__}(country={self.country!r}, length={self.length!r},' \
                   f' width={self.width!r}, power={self.power!r})'

        @property
        def tax(self):
            """возвращает размер налога на авто"""
            return f'{self.power * 24} рублей'


    class BMW(Car):
        """дочерний класс"""
        def __init__(self, country: str, length: int, width: int, power: int, color: str, brand: str,
                     typeb: str):
            """
            метод конструктор
            brand -- марка производителя
            typeb -- тип стула. Например: барный, складной, кухонный, табурет и т.д.
            """
            super().__init__(country, length, width, power, color)
            self.brand = brand
            self.typeb = typeb

        def __str__(self):
            """возвращает экземпляр класса"""
            tstr = super().__str__()
            return f'Предмет мебели: {self.__class__.__name__}. {tstr}, Марка производителя: {self.brand}. ' \
                   f'Тип стула: {self.typeb}'

        def __repr__(self):
            """метод, возвращающий валидную Python строку точно такого же экземпляра"""
            return f'{self.__class__.__name__}(country={self.country!r}, length={self.length!r},' \
                   f' width={self.width!r}, power={self.power!r}, brand={self.brand!r},' \
                   f' car_body_type={self.typeb!r})'


    M8 = BMW("Germany", 1362, 4867, 625, "Wildcherry", "BMW", "coupe")
    print(M8.tax)
