from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import sp


class Mensagem(BoxLayout):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Definir(tarefa))


class Definir(BoxLayout):
    def __init__(self, texto='',**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.add_widget(
            Button(
                size_hint = (None, None),
                width=100,
                border=(0, 0, 0, 0),
                background_normal = 'cayla_rosa.png',
                background_down = 'cayla_rosa.png'
            ))
        self.add_widget(Adaptavel(texto))


class Adaptavel(Button):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.font_size = sp(30)
        self.text = texto
        self.background_normal = 'balao_rosa.png'
        self.background_down = 'balao_rosa.png'

    def on_size(self, *args):
        self.text_size = (self.width - sp(30), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)
        self.width += sp(30)
        if self.width > 550:
            self.size_hint = (1, None)



class Test(App):
    def build(self):
        return Mensagem([
            'Coisas para fazer hoje :)',
            'Comprar pão',
            'Compra mascara',
            ':)',
            'sedjfjfgofoajfoasofaosjfsoajfosajfjsafjasofjaosjfoasjf'
        ])

Test().run()