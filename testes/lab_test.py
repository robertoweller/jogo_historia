from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.metrics import sp


class Mensagem(BoxLayout):
    def __init__(self,tarefas,**kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Adaptavel(tarefa))


class Definir(BoxLayout):
    def __init__(self, texto='',**kwargs):
        super().__init__(**kwargs)
        self.ids.lab.text=texto



class Adaptavel(Label):
    def __init__(self, texto, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.font_size = sp(30)
        self.text = texto

    def on_size(self, *args):
        self.text_size = (self.width - sp(10), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)



class Test(App):
    def build(self):
        return Mensagem(['Fazer compras','Buscar filho','Molhar a calçada','iu','iuhyfhiahfawfoiahsfihsfihasfhasihfoi doadjoajdoajsj'
        'ojfopsajfosjfpoasfjpasfj'
        'fpafpasf',
        'dshgfihfgigiahg',
        'jaosjfaojgjasgosagjasop'
        'jfoajfoasfoajf',
        'fajfiajfgiaj',
        'ejfggiagi',
        'effijfiajsfi',
        'asofjopasfjopasf',
        'iug'])

Test().run()