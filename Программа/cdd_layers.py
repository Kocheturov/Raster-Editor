class LayerManager:
    def __init__(self):
        self.layers = []

    def create_layer(self, name="New Layer"):
        # Создание нового слоя
        new_layer = Layer(name)
        self.layers.append(new_layer)
        return new_layer

    def delete_layer(self, layer_index):
        # Удаление слоя по индексу
        if 0 <= layer_index < len(self.layers):
            del self.layers[layer_index]
        else:
            raise ValueError("Invalid layer index")

    def duplicate_layer(self, layer_index):
        # Дублирование слоя по индексу
        if 0 <= layer_index < len(self.layers):
            layer_copy = self.layers[layer_index].copy()
            self.layers.append(layer_copy)
        else:
            raise ValueError("Invalid layer index")
