from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout


'''
Ler sober o jogo no arquivo README.md
'''


class Mensagem(ScrollView):
    def __init__(self, mensagem, **kwargs):
        super().__init__(**kwargs)
        self.todas_mensagnes = len(mensagem)
        self.conta = 0
        # Adicionar uma lista para inverter?
        # A classe incial estará esperando a classe mensagem como argumento
        # Dentro de mensagem ficara o conteudo daclasse Conteudo e será adicionado o widget da mensagem.
        print(mensagem[0])
        # for mensagem in mensagem:
        #     self.ids.men.add_widget(Conteudo(text=mensagem))

        def chama_mensagem():
            if self.conta < self.todas_mensagnes:
                print(mensagem[0])
                self.conta += 1


class Conteudo(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        # e o conteudo espera text como arguemnto que é passado na classe mensagem
        # se não for passado nada, terá texto vazio ''
        self.ids.lab.text = text


class PerdiTubes(App):
    def build(self):
        return Mensagem(['Olá eu sou a pessoa inventada \npara explicar esse jogo',
                         'Esse é um texto que passa a '
                         '\ncaixa de mensagem espero poder '
                         '\nresolver logo isso',
                         'Viu? Tem muita coisa que \nprecisa ser melhorada',
                         'O foco de agora é trabalhar \nnessas mensagens que vão vão \nsubir',
                         'Já é possivel \nrolar o texto quando quando as \nmensagens passa a tela'
                         ])


if __name__ == '__main__':
    PerdiTubes().run()