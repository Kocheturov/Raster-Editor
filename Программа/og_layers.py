class LayerManager:
    # ... (методы create_layer, delete_layer, duplicate_layer)

    def move_layer(self, from_index, to_index):
        """
        Перемещает слой с одного индекса на другой.

        Аргументы:
            from_index (int): Индекс слоя, который нужно переместить.
            to_index (int): Индекс, на который нужно переместить слой.

        Вызывает:
            ValueError: Если индексы слоев неверны.
        """
        # Перемещение слоя
        if 0 <= from_index < len(self.layers) and 0 <= to_index < len(self.layers):
            layer = self.layers.pop(from_index)
            self.layers.insert(to_index, layer)
        else:
            raise ValueError("Invalid layer index")

    def group_layers(self, layer_indices):
        """
        Группирует слои с указанными индексами.

        Аргументы:
            layer_indices (list): Список индексов слоев для группировки.
        """
        # Группировка слоёв
        # ...
