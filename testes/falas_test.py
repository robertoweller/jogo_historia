# Arquivo test.kv é daqui
from kivy.app import App
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Mensagem(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        self.con = 0
        # Se for True, não vai adicionar a imagem na quarta vez
        # Se for False, vai adicionar balão  imagem normalmente
        self.img = True
        for tarefa in tarefas:
            self.con += 1
            # Quando a contagem chega à 4, só adiciona o balão
            if self.img:
                if self.con < 4:
                    # Quando a contagem é menor de 4
                    # Adiciona o balão e a imagem da Cayla jutos
                    self.ids.box.add_widget(CaylaFala(tarefa))
                else:
                    # Quando chega à 4 adiciona apenas o balão, e volta a contar
                    self.ids.box.add_widget(Adaptavel(tarefa))
                    self.con = 0
            else:
                self.ids.box.add_widget(CaylaFala(tarefa))

# Classe Cayla [Cayla + adiciona(balão)]
class CaylaFala(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        # Adiciona o balão do desse lado ->
        self.add_widget(Adaptavel(texto))


# Não usada por enquanto
class Cayla(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.border = (0, 0, 0, 0)
        self.background_normal = 'cayla_rosa.png'
        self.background_down = 'cayla_rosa.png'


# classe do balão
class Adaptavel(Button):
    largura = 400
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.larg = 0
        self.size_hint = (None, None)
        self.font_size = sp(30)
        self.text = texto
        self.background_normal = 'balao_rosa.png'
        self.background_down = 'balao_rosa.png'

    # Cada vez que a largura for mudada esse evento é chamado
    def on_width(self, *args):
        self.larg += 1
        print(f'{self.larg} linhas')

    def on_size(self, *args):
        self.text_size = (self.width - sp(30), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)
        self.width += sp(30)
        if self.width > self.largura:
            self.width = self.largura


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
