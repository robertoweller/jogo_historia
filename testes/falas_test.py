# Arquivo test.kv é daqui
from kivy.app import App
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


# Não usada por enquanto
class Cayla(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.border = (0, 0, 0, 0)
        self.background_normal = 'cayla_rosa.png'
        self.background_down = 'cayla_rosa.png'


class Mensagem(BoxLayout):
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        self.con = 0
        # Se for True, não vai adicionar a imagem na quarta vez
        # Se for False, vai adicionar balão  imagem normalmente
        self.img = False
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
                # self.ids.box.add_widget(CaylaFala(tarefa))
                self.ids.box.add_widget(MeuBalao(tarefa))


# Cayla [Cayla + adiciona(balão)]
class CaylaFala(BoxLayout):
    def __init__(self, texto='',**kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.padding=(10, 10, 0, 0)
        self.spacing = 10
        self.padding= (0, 20, 0, 10)
        self.add_widget(
            Button(
                size_hint = (None, None),
                pos_hint={'top':1.20},
                width=100,
                border=(0, 0, 0, 0),
                background_normal = 'cayla_rosa.png',
                background_down = 'cayla_rosa.png'
            ))
        # Adiciona o balão do desse lado ->
        self.add_widget(Adaptavel(texto))


# Balão da Cayla
class Adaptavel(Button):
    largura = 400
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.larg = 0
        self.size_hint = (None, None)
        self.font_size = sp(30)
        self.text = texto
        self.pos_hint = {'bottom': 1}
        self.background_normal = 'baloes/balao_rosa.png'
        self.background_down = 'baloes/balao_rosa.png'

    def on_size(self, *args):
        self.text_size = (self.width - sp(30), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)
        self.width += sp(30)
        if self.width > self.largura:
            self.width = self.largura
            # CaylaFala.height = 100


# Classe do jogador
class MeuBalao(Button):
    largura = 400
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.larg = 0
        self.size_hint = (None, None)
        self.font_size = sp(30)
        self.text = texto
        self.pos_hint = {'bottom': 1}
        self.background_normal = 'baloes/balao_azul.png'
        self.background_down = 'baloes/balao_azul.png'

    def on_size(self, *args):
        self.text_size = (self.width - sp(30), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)
        self.width += sp(30)
        if self.width > self.largura:
            self.width = self.largura
            # CaylaFala.height = 100


class Test(App):
    def build(self):
        return Mensagem([
            'Coisas para fazer hoje :))))))',
            'Comprar pão',
            ':)',
            'Bolacha',
            'sedjfjfgofoajrfanfanafpojafafjoasfopfojajfpoafopajfopafjasopffasflslflf'
            'sflsfkafosfksoafkosakfoksfokofkoaskfosakfoskfosakfopksafopksaofpksaofka',
            'Agora falando sério',
            'Quero compra sla, algo que não me lembro'
        ])

Test().run()
