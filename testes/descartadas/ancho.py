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
               

class Widgets(AnchorLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.anchor_x='right'
        self.anchor_y='bottom'
        # AnchorLayout vai ficar dentro do BoxLayout
        

        # Se não der certo vou usar o label para empurrar ->
        # self.add_widget(Label(size_hint=(1, 1))

        #self.orientation = 'horizontal'
        self.size_hint_y = None
        #self.size_hint_x = None
        
        
        self.add_widget(Button(
                text=texto, 
                font_size=30, 
                size_hint=(None,None),
                height=100,
                width=100,
                

            ))
        self.add_widget(Label(
            text= 'AAAA', 
            size_hint=(None, None), 
            height=100, 
            width=100
            ))

        # self.add_widget(Label(size_hint=(1, 1)))



class AssimAnchor(App):
    def build(self):
        return Mensagem(['A', 'B', 'C'])

AssimAnchor().run()