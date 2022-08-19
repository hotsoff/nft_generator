import os
from layer import Layer
from PIL import Image
from typing import List


class PicGenerator:

    def __init__(self, images_path: str):
        self.layers: List[Layer] = self.load_image_layers(images_path)
        self.background_color = (120, 150, 180)
        self.output_path: str = 'output'
        os.makedirs(self.output_path, exist_ok=True)

    def load_image_layers(self, images_path: str):
        sub_paths = os.listdir(images_path)
        print(sub_paths)
        layers = []
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            layer = Layer(layer_path)
            layers.append(layer)
        return layers

    def generate_image_sequence(self):
        image_path_sequence = []
        for layer in self.layers:
            image_path = layer.get_random_image_path()
            image_path_sequence.append(image_path)

        return image_path_sequence

    def render_pic_image(self, image_path_sequence: List[str]):
        image = Image.new('RGBA', (24, 24), self.background_color)
        for image_path in image_path_sequence:
            layer_image = Image.open(image_path)
            image = Image.alpha_composite(image, layer_image)
        return image

    def save_image(self, image: Image.Image):
        image_file_name = 'pic.png'
        image_save_path = os.path.join(self.output_path, image_file_name)
        image.save(image_save_path)

    def generate_pic(self):
        print('get started')
        image_path_sequence = self.generate_image_sequence()
        image = self.render_pic_image(image_path_sequence)
        self.save_image(image)