# assimanchor.kv é daqui
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout


# Teste para entender o AnchorLayout
class Mensagem(BoxLayout):
    """return: Lista de Button"""
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Widgets(tarefa))
              

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

class Original(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.size_hint_y = None
        # self.height = self.height

        # E AnchorLayout vai ficar dentro da BoxLayout raiz
        self.acho = AnchorLayout(
            anchor_x='right', 
            anchor_y='top',
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
        #self.height=largura.height

        # self.box vai ficar dentro de self.pri
        self.pri.add_widget(self.box)
        
        
        # self.pri.size_hint_y = self.pri.size_hint_max_y

        #  BoxLayout vai ficar dentro do AnchorLayout
        self.acho.add_widget(self.pri)
        
        self.add_widget(self.acho)


class AssimAnchor(App):
    def build(self):
        return Mensagem(['A', 'B', 'C'])

AssimAnchor().run()