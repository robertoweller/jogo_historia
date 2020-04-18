from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class TestTexto(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Botão do meio se adapta à quantidades de letras (só na largura do botão)
        self.ids.bot.text_size[0] = 20*len(self.ids.bot.text)-30
        self.ids.box.width = f'{20*len(self.ids.bot.text)}px'
        self.ids.bot1.text_size[0] = 20*len(self.ids.bot1.text)-30
        self.ids.box1.width = f'{20*len(self.ids.bot1.text)}px'


class MeuPrograma(App):
    def build(self):
        
        return TestTexto()



if __name__ == '__main__':
    MeuPrograma().run()
