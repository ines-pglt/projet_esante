from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class ImageZoomApp(App):
    def build(self):
        layout = FloatLayout()
        scatter = Scatter(do_rotation=False, do_translation=False, do_scale=True)
        image = Image(source='image_alex.jpg')
        scatter.add_widget(image)
        layout.add_widget(scatter)
        return layout

if __name__ == '__main__':
    ImageZoomApp().run()

