class Box:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """
        Создание и подготовка к работе объекта "Стакан"
        :param capacity_volume: Объем коробки
        :param occupied_volume: Объем занятого пространства в коробке
        """
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def is_box(self) -> bool:
        """
        Функция которая проверяет является ли словарь коробкой
        :return: Является ли объект коробкой или нет
        """

        ...

    def add_toys_to_box(self, toys: int) -> None:
        """
         Добавление игрушек в коробку.
        Если количество игрушек превышает доступное место,
        то возвращается количество непоместившихся игрушек
        :param toys: Объем добавляемых игрушек
        :return: Объем непоместившихся игрушек
        """

        ...

    def remove_toys_from_box(self, estimate_toys: int) -> int:
        """
        Извлечение игрушек из коробки
        Если количество извлекаемых игрушек превышает количество игрушек в коробке,
        то возвращается реальное количество извлеченных игрушек
        :param estimate_toys: Объем извлекаемых игрушек
        :return: Объем реально извлеченных игрушек
        """
        ...



