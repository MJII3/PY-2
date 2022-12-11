class Bottle:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        """
        Создание и подготовка к работе объекта "Бутылка"
        :param capacity_volume: Объем бутылки
        :param occupied_volume: Объем занимаемой жидкости
         Примеры:
        >>> bottle = Bottle(500, 0)  # инициализация экземпляра класса
        """

    if not isinstance(capacity_volume, (int, float)):
        raise TypeError("Объем бутылки должен быть типа int или float")
    if capacity_volume <= 0:
        raise ValueError("Объем бутылки должен быть положительным числом")
    self.capacity_volume = capacity_volume

    if not isinstance(occupied_volume, (int, float)):
        raise TypeError("Количество жидкости должно быть int или float")
    if occupied_volume < 0:
        raise ValueError("Количество жидкости не может быть отрицательным числом")
    self.occupied_volume = occupied_volume

    def is_bottle(self) -> bool:
        """
        Функция которая проверяет является ли словарь бутылка
        :return: Является ли объект бутылкой или нет
        """
        ...

    def add_water_to_bottle(self, water: int) -> int:
        """
        Добавление воды в бутылку.
        Если количество добавляемой жидкости превышает доступное место,
        то возвращается количество непоместившейся жидкости
        :param water: Объем добавляемой жидкости
        :return: Объем непоместившейся жидкости
        """
        ...

    def remove_water_from_bottle(self, estimate_water: int) -> int:
        """
        Извлечение воды из бутылки
        Если количество извлекаемой жидкости превышает количество воды в бутылке,
        то возвращается реальное количество извлеченной воды
        :param estimate_water: Объем извлекаемой жидкости
        :return: Объем реально извлеченной жидкости
        """
        ...


if __name__ == "__main__":
    doctest.testmod()