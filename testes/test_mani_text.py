from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class TestTexto(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Se tiver menos que 3 caracters vai ter um tamanho unico
        if len(self.ids.bot.text) < 3:
            # Botão do meio se adapta à quantidades de letras (só na largura do botão)
            self.ids.bot.text_size[0] = 20*3-30
            self.ids.box.width = f'{20*3}px'
        else:
            self.ids.bot.text_size[0] = 20*len(self.ids.bot.text)-30
            self.ids.box.width = f'{20*len(self.ids.bot.text)}px'

        if len(self.ids.bot.text) < 3:
            # Botão do meio se adapta à quantidades de letras (só na largura do botão)
            self.ids.bot1.text_size[0] = 20*3-30
            self.ids.box1.width = f'{20*3}px'
        else:
            self.ids.bot1.text_size[0] = 20*len(self.ids.bot1.text)-30
            self.ids.box1.width = f'{20*len(self.ids.bot1.text)}px'
        # E assim vai... só falt por no código original. A lógica é que cada widget adcionado tenha seu tamanho automatico de acordo com a quantidade de caracters

class MeuPrograma(App):
    def build(self):
        
        return TestTexto()



if __name__ == '__main__':
    MeuPrograma().run()
