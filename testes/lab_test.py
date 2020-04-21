from kivy.app import App
from kivy.metrics import sp
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Mensagem(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        
        for tarefa in tarefas:
            self.ids.box.add_widget(CaylaFala(tarefa))


class CaylaFala(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding=(0, 0, 0, 10)
        self.spacing = 10
        
        self.add_widget(Button(
            size_hint = (None, None),
            width = 100,
            border = (0, 0, 0, 0),
            background_normal = 'cayla_rosa.png',
            background_down = 'cayla_rosa.png'
        ))
        self.add_widget(Adaptavel(texto))

# Testando reaproveitamento de widget
class Cayla(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width = 100
        self.border = (0, 0, 0, 0)
        self.background_normal = 'cayla_rosa.png'
        self.background_down = 'cayla_rosa.png'


class Adaptavel(BoxLayout, Button):
    largura = NumericProperty(400)
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.font_size = sp(30)
        self.text = texto
        self.background_normal = 'balao_rosa.png'
        self.background_down = 'balao_rosa.png'
    # Teste para entender os eventos
    def on_width(self, *args):
        print('sla')
    def on_size(self, *args):
        self.text_size = (self.width - sp(30), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)
        self.width += sp(30)
        if self.width > self.largura:
            self.width = self.largura

            # self.ids.imagem.background_normal = None
            # self.ids.imagem.background_down = None


class Test(App):
    def build(self):
        return Mensagem([
            'Coisas para fazer hoje :))))))',
            'Comprar pão',
            ':)',
            'sedjfjfgofoajrfanfanafpojafafjoasfopfojajfpoafopajfopafjasopff',
            ':))'
        ])

Test().run()
