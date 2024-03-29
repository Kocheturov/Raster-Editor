class LayerManager:
    # ... (методы create_layer, delete_layer, duplicate_layer)

    def move_layer(self, from_index, to_index):
        # Перемещение слоя
        if 0 <= from_index < len(self.layers) and 0 <= to_index < len(self.layers):
            layer = self.layers.pop(from_index)
            self.layers.insert(to_index, layer)
        else:
            raise ValueError("Invalid layer index")

    def group_layers(self, layer_indices):
        # Группировка слоёв
        # ...
