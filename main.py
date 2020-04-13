from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


'''
Ler sober o jogo no arquivo README.md
'''


class Mensagem(ScrollView):
    def __init__(self, mensagem, **kwargs):
        super().__init__(**kwargs)
        self.mensagem = mensagem
        self.todas_mensagnes = len(mensagem)
        self.conta = 0
        # Adicionar uma lista para inverter?
        # A classe incial estará esperando a classe mensagem como argumento
        # Dentro de mensagem ficara o conteudo daclasse Conteudo e será adicionado o widget da mensagem.
        Clock.schedule_interval(self.chama_mensagem, 4)
        # for mensagem in mensagem:
        #     self.ids.men.add_widget(Conteudo(text=mensagem))

        # Vai adicionar uma a uma as mensagens

    def chama_mensagem(self, sla):
        if self.conta < self.todas_mensagnes:
            print(self.mensagem[self.conta])
            self.ids.men.add_widget(Conteudo(text=self.mensagem[self.conta]))
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