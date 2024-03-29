class LayerManager:
    """
    Класс для управления слоями, включая создание, удаление и 
    дублирование.
    """

    def __init__(self):
        """
        Инициализирует экземпляр LayerManager с пустым списком слоев.
        """
        self.layers = []

    def create_layer(self, name="New Layer"):
        """
        Создает новый слой с заданным именем и добавляет его в список 
        слоев.

        Аргументы:
            name (str, optional): Имя нового слоя. По умолчанию "New Layer".

        Возвращает:
            Layer: Созданный слой.
        """
        # Создание нового слоя
        new_layer = Layer(name)
        self.layers.append(new_layer)
        return new_layer

    def delete_layer(self, layer_index):
        """
        Удаляет слой по его индексу.

        Аргументы:
            layer_index (int): Индекс слоя для удаления.

        Вызывает:
            ValueError: Если индекс слоя неверен.
        """
        # Удаление слоя по индексу
        if 0 <= layer_index < len(self.layers):
            del self.layers[layer_index]
        else:
            raise ValueError("Invalid layer index")

    def duplicate_layer(self, layer_index):
        """
        Дублирует слой по его индексу и добавляет копию в список слоев.

        Аргументы:
            layer_index (int): Индекс слоя для дублирования.

        Вызывает:
            ValueError: Если индекс слоя неверен.
        """
        # Дублирование слоя по индексу
        if 0 <= layer_index < len(self.layers):
            layer_copy = self.layers[layer_index].copy()
            self.layers.append(layer_copy)
        else:
            raise ValueError("Invalid layer index")
