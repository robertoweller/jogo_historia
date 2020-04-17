from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class TestTexto(BoxLayout):
    pass


class MeuPrograma(App):
    def build(self):
        return TestTexto()



if __name__ == '__main__':
    MeuPrograma().run()
