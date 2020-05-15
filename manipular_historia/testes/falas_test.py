# Arquivo test.kv é daqui
from kivy.app import App
from kivy.metrics import sp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config


def setup():

    # Seta uma largura e altura and para a janela
    Config.set('graphics', 'width', '720')
    Config.set('graphics', 'height', '1280')

    # Se for 0, não será possivel redimensionar e se for 1 será
    Config.set('graphics', 'resizable', '1')
    # Descomente essa linha para deixa tela cheia
    # Config.set('graphics', 'fullscreen', 'auto')
    Config.write()


# Não usada por enquanto
class Personagem(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.border = (0, 0, 0, 0)
        self.background_normal = 'cayla_rosa.png'
        self.background_down = 'cayla_rosa.png'


class Mensagem(BoxLayout):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.con = 0
        self.eu_balao = 'baloes/eu_baixo.png'
        self.cayla_balao = 'baloes/cay_baixo.png'
        # Se for True, não vai adicionar a imagem na quarta vez
        # Se for False, vai adicionar balão  imagem normalmente
        self.img = False
        for tarefa in texto:
                self.ids.box.add_widget(EuFala(texto=tarefa))


# Personagem [Personagem + adiciona(balão)]
class PersonFala(BoxLayout):

    def __init__(self, texto='', person='', balao ='', eu=False, **kwargs):

        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 15
        # self.padding= (0, 0, 0, 0)
        self.top = 1
        self.size_hint = (None, None)
        self.pos_hint = {'x':2.69, 'y':0}
        # Se for eu, vai add minha classe, se não será a classe da cayla
        if eu:
            print('eu')
<<<<<<< Updated upstream:manipular_historia/testes/falas_test.py
            self.add_widget(Label())
=======
            
>>>>>>> Stashed changes:testes/falas_test.py
            self.add_widget(
                # Add balão desse lado <-
                Adaptavel(
                    texto=texto,
                    balao=balao
                    ))
            # Personagem usado
            self.add_widget(
                Button(
                    size_hint = (None, None),
                    #pos_hint={'center':self.top},
                    border=(0, 0, 0, 0),
                    background_normal = person,
                    background_down = person))
        else:
            # Personagem da Cayla
            self.add_widget(
            Button(
                    size_hint = (None, None),
                    #pos_hint={'center':self.top},
                    border=(0, 0, 0, 0),
                    background_normal = person,
                    background_down = person
                ))
            
            # Adiciona o balão do desse lado ->
            self.add_widget(
                Adaptavel(
                    texto=texto,
                    balao=balao
                    ))


class EuFala(BoxLayout):
    def __init__(self, texto='', person='modelo.png', balao='baloes/eu_baixo.png', **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Adaptavel(texto=texto, balao=balao))
        self.add_widget(Button(
                    size_hint = (None, None),
                    #pos_hint={'center':self.top},
                    border=(0, 0, 0, 0),
                    background_normal = person,
                    background_down = person))

# Balão dos personagens
class Adaptavel(Button):
    largura = 400
    def __init__(self, texto, balao, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.font_size = sp(30)
        self.text = texto
        # self.pos_hint = {'bottom': 1}
        self.pos_hint = {'right':1}
        self.background_normal = balao
        self.background_down = balao
        
    def on_size(self, *args):
        self.text_size = (self.width - sp(30), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)
        self.width += sp(30)
        if self.width > self.largura:
            self.width = self.largura


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


class Test(App):
    def build(self):
        return Mensagem([
            'Fala testeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee \n\n\n\n',
            'Fala teste \n\n\n\n'
        ])
setup()
Test().run()
