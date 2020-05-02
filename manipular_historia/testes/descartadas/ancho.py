# assimanchor.kv é daqui
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.metrics import sp


# Teste para entender o AnchorLayout
class Mensagem(BoxLayout):
    """return: Lista de Button"""
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(TesteBox(texto=tarefa))
              

class Widgets(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        # self.height = self.height

        # E AnchorLayout vai ficar dentro da BoxLayout raiz
        self.acho = AnchorLayout(
            anchor_x='right', 
            anchor_y='bottom',
            size_hint_min_y = None)

        self.box = BoxLayout(
            orientation='horizontal',
            spacing = 10,
            size_hint_y = None,
            height=100)
        
        # No código original é o adaptavel
        self.box.add_widget(Label(
            text= 'Letra',
            size_hint=(None, None),
            height=100,
            width=100
            ))
        
        self.box.add_widget(Button(
                text=texto, 
                font_size=30, 
                size_hint=(None,None),
                height=100,
                width=100,
            ))
        
        self.lag1 = 0
        self.alt1 = 0
        self.ss = True
        
        # Calcula a largura dos dois Widgets
        for largura in self.box.children[:]:
            
            if self.ss:
                self.lag1 = largura.width
                self.alt1 = largura.height
                # print(largura.width)
                self.ss = False
            else:
                self.lag1 += largura.width
                self.alt1 += largura.height
        
        self.pri = BoxLayout(
            size_hint_x = None,
            size_hint_y = None,
            width=self.lag1)
            
        self.pri.add_widget(self.box)

        #  BoxLayout vai ficar dentro do AnchorLayout
        self.acho.add_widget(self.pri)
        
        self.add_widget(self.acho)


class TesteBox(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Adaptavel(texto=texto))
        self.add_widget(Button(
                    size_hint = (None, None),
                    #pos_hint={'center':self.top},
                    border=(0, 0, 0, 0),
                    background_normal = 'cayla_rosa.png',
                    background_down = 'cayla_rosa.png'))


class Original(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.size_hint_max_y = None
        # Controla a altura do BoxLayout
        #self.height = 150

        # E AnchorLayout vai ficar dentro da BoxLayout raiz
        self.acho = AnchorLayout(
            anchor_x='right', 
            anchor_y='top',
            size_hint_min_y = None)

        self.box = BoxLayout(
            orientation='horizontal',
            spacing = 10,
            size_hint = (None, None))
        
        # No código original é o adaptavel (é do balão essa classe)
        self.box.add_widget(Adaptavel(
                    texto=texto,
                    balao='eu_baixo.png'
                    
            ))
        
        self.box.add_widget(Button(
                text='P', 
                font_size=30, 
                size_hint=(None,None),
                height=100,
                width=100,
            ))
        
        self.lag1 = 0
        self.alt1 = 0
        self.alt2 = 0
        self.ss = True
        
        # Calcula a largura dos dois Widgets
        for largura in self.box.children[:]:
            
            if self.ss:
                self.lag1 = largura.width
                self.alt1 = largura.height
                # print(largura.width)
                self.ss = False
            else:
                self.lag1 += largura.width
                # self.alt1 += largura.height
                print(
                f'\nwidth = {self.lag1}\n'
                f'height = {self.alt1}\n'
                )
        # Aqui que a guerra começa
        self.pri = BoxLayout(
            size_hint_x = None,
            size_hint_y = None,
            width=self.lag1
            )
        
        # Altura do BoxLayout vai ser a altura do widgets que mais muda.
        
        # No caso é o botão
        # Minha camada raiz está travada na altura dos widgtes
        # Mas por algum motivo quando os widtes almenta de altura
        # a altura não é convertida aqui
        self.height=self.alt1
        #self.width= self.lag1

        # self.box vai ficar dentro de self.pri
        # self.pri.add_widget(self.box)
        
        
        # self.pri.size_hint_y = self.pri.size_hint_max_y

        #  BoxLayout vai ficar dentro do AnchorLayout
        self.acho.add_widget(self.box)
        
        self.add_widget(self.acho)


# Balão dos personagens
class Adaptavel(Button):
    largura = 400
    def __init__(self, texto='', balao='eu_baixo.png', **kwargs):
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


class BoxTeste(BoxLayout):
    pass


class AssimAnchor(App):
    def build(self):
        return Mensagem(['Aaaaaaaaaaaaaaaaaa', 'B', 'C', 'E', 'F', 'G', 'H'])

AssimAnchor().run()