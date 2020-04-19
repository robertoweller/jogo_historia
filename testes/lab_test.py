from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
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
        self.add_widget(Adaptavel(texto))
        self.add_widget(CheckBox())



class Adaptavel(Button):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.font_size = sp(30)
        self.text = texto
        self.background_normal = 'balao_rosa.png'
        self.background_down = 'balao_rosa.png'

    def on_size(self, *args):
        self.text_size = (self.width - sp(30), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)



class Test(App):
    def build(self):
        return Mensagem([
            'Coisas para fazer hoje :)',
            'Comprar pão',
            'Compra pessa',
            'Ir buscar uma mascara personalizada',
            'Terminar programa'
        ])

Test().run()