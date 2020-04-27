from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

# Teste para entender o AnchorLayout

class Mensagem(BoxLayout):
    """return: Lista de Button"""
    def __init__(self, tarefas, **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Button(text=tarefa,font_size=30,size_hint_y=None,height=200))
               

class AssimAnchor(App):
    def build(self):
        return Mensagem(['A', 'B'])

AssimAnchor().run()