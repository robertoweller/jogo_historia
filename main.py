from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout


'''
Ler sober o jogo no arquivo README.md
'''


class Mensagem(ScrollView):
    def __init__(self, mensagem, **kwargs):
        super().__init__(**kwargs)
        # A classe incial estará esperando a classe mensagem como argumento
        # Dentor de mensagem ficara o conteudo daclasse Conteudo e será adicionado o widget da mensagem.
        for mensagem in mensagem:
            self.ids.men.add_widget(Conteudo(text=mensagem))


class Conteudo(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        # e o conteudo espera text como arguemnto que é passado na classe mensagem
        # se não for passado nada, terá texto vazio ''
        self.ids.lab.text = text


class PerdiTubes(App):
    def build(self):
        return Mensagem(['Testando',
                         'Aqui terá uma mensagem!',
                         'Esse é um texto que passa a '
                         '\ncaixa de mensagem espero poder '
                         '\nresolver logo isso',
                         'Outra mensagem adicionada'
                         ])


if __name__ == '__main__':
    PerdiTubes().run()