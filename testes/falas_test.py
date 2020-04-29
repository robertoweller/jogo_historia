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
            self.con += 1
            # Quando a contagem chega à 4, só adiciona o balão
            if self.img:
                if self.con < 4:
                    # Quando a contagem é menor de 4
                    # Adiciona o balão e a imagem da Cayla jutos
                    self.ids.box.add_widget(PersonFala(
                        tarefa=tarefa,
                        person='cayla_rosa.png'
                        ))
                else:
                    # Quando chega à 4 adiciona apenas o balão, e volta a contar
                    self.ids.box.add_widget(Adaptavel(
                        texto = tarefa,
                        balao = self.cayla_balao))
                    self.con = 0
            else:
                # self.ids.box.add_widget(CaylaFala(tarefa))
                
                self.ids.box.add_widget(PersonFala(
                    eu=True,
                    texto=tarefa, 
                    person='cayla_rosa.png',
                    balao = self.eu_balao
                    ))

# Personagem [Personagem + adiciona(balão)]
class PersonFala(BoxLayout):

    def __init__(self, texto='', person='', balao ='', eu=False, **kwargs):

        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = 15
        # self.padding= (0, 0, 0, 0)
        self.top = 1
        self.size_hint = (None, None)
        self.pos_hint = {'x':2.02, 'y':0}
        # Se for eu, vai add minha classe, se não será a classe da cayla
        if eu:
            print('eu')
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


# Personagem [Personagem + adiciona(balão)]
# Classe adicionada para testar
class AnchoFala(BoxLayout):
    def __init__(self, texto='', person='', balao ='', eu=False, **kwargs):

        super().__init__(**kwargs)
        #self.size_hint_y = None
        self.apaga = BoxLayout()
        self.acho = AnchorLayout(
            anchor_x='right', 
            anchor_y='top',
            size_hint_min_y = None)
        
        self.box = BoxLayout(
            orientation='horizontal', 
            spacing = 10,
            size_hint_y = None,
            height=100)

        # Se for eu, vai add minha classe, se não será a classe da cayla
        if eu:
            print('eu')
            self.apaga.add_widget(
                # Add balão desse lado <-
                Adaptavel(
                    texto=texto,
                    balao=balao
                    ))
            # Personagem usado
            self.box.add_widget(
                Button(
                    size_hint = (None, None),
                    pos_hint={'center':self.top},
                    border=(0, 0, 0, 0),
                    background_normal = person,
                    background_down = person))
        else:
            # Personagem da Cayla
            self.box.add_widget(
            Button(
                    height=100,
                    width=100,
                    size_hint = (None, None),
                    pos_hint={'center':self.top},
                    border=(0, 0, 0, 0),
                    background_normal = person,
                    background_down = person
                ))
            self.box.add_widget(
                Label(
                    text=texto,
                    font_size=30,
                    height=100,
                    width=100,
                    size_hint = (None, None)
                )
            )

            # Adiciona o balão do desse lado ->
            self.apaga.add_widget(
                Adaptavel(
                    texto=texto,
                    balao=balao
                    ))
        
        self.lag1 = 0
        self.ss = True
        
        # Calcula a largura dos dois Widgets
        for largura in self.box.children[:]:
            
            if self.ss:
                self.lag1 = largura.width
                # print(largura.width)
                self.ss = False
            else:
                self.lag1 += largura.width
        
        self.pri = BoxLayout(
            size_hint_x = None,
            size_hint_y = None,
            width=self.lag1)

        self.pri.add_widget(self.box)

        #  BoxLayout vai ficar dentro do AnchorLayout
        self.acho.add_widget(self.pri)
        
        self.add_widget(self.acho)

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
            ' aaa.aa..',
            ' saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        ])
setup()
Test().run()
