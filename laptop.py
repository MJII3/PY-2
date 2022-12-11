class Laptop:
    def __init__(self, available_memory: int, full_memory: int):
        """
        Создание и подготовка к работе объекта "Ноутбук"
        :param available_memory: Объем памяти
        :param full_memory: Объем занимаемой памяти
        """
        self.available_memory = available_memory
        self.full_memory = full_memory
        ...

    def is_laptop(self) -> bool:
        """
        Функция которая проверяет является ли словарь ноутбуком
        :return: Является ли объект ноутбуком или нет
        """
        ...

    def download_photos_to_laptop(self, photos: float) -> None:
        """
        Скачивание фотографий на ноутбук.
        Если вес скачиваемых фото превышает доступное место,
        то возвращается количество непоместившейся фото
        :param photos: Объем скачиваемых фото
        :return: Объем непоместившихся фото
        Примеры:
        >>> laptop = Laptop (500, 0)
        >>> laptop.download_photos_to_laptop(200)
        """
        if not isinstance( photos, (int, float)):
            raise TypeError("Добавляемые фото должны быть типа int или float")
        if photos < 0:
            raise ValueError("Добавляемые фото должна положительным числом")
        ...

    def delete_photos_from_laptop(self, volume_to_be_deleted: int) -> int:
        """
        Удаление фотографий из ноутбука
        Если количество удаляемых фото превышает количество фото в ноутбуке,
        то возвращается реальное количество удалённых фото
        :param volume_to_be_deleted: Объем удаляемых фото
        :return: Объем реально удалённых фото
        """
        ...


if __name__ == "__main__":
    doctest.testmod()