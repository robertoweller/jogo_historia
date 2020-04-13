from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

'''
Ler sobre o jogo no arquivo README.md
'''


class Mensagem(ScrollView):
    def __init__(self, mensagem, **kwargs):
        super().__init__(**kwargs)
        # A classe incial estará esperando a classe mensagem como argumento
        # Essa é aquela mensagem da lista da classe PerdiTubes
        self.mensagem = mensagem
        self.todas_mensagnes = len(mensagem)
        self.conta = 0
        self.fala = []


        # O Clock atende o que eu quero, que é adicionar uma mensagem, depois de 4 segundo adiciona outra.
        Clock.schedule_interval(self.chama_mensagem, 4)

        # O for abaixo adicionava tudo de uma fez só
        # for mensagem in mensagem:
        #     self.ids.men.add_widget(Conteudo(text=mensagem))

        # Vai adicionar uma a uma as mensagens

    def chama_mensagem(self, sla):

        # Quando acabar as mensagens vai parar de adicionar os widgets, isso é para não dar erro.
        if self.conta < self.todas_mensagnes:
            # Nessa narrativa são duas pessoas, mas da para adicionar mais pessoas
            falas = {
                '#cay': CaylaFala(text=self.mensagem[self.conta][4:]),
                '#euu': EuFala(text=self.mensagem[self.conta][4:])
            }

            # print(self.mensagem[self.conta])

            # Procura dentro da biblioteca quem está falando
            self.ids.men.add_widget(falas[self.mensagem[self.conta][:4]])
            # Nesse print mostra quem está falando no momento
            print(self.mensagem[self.conta][:4])
            self.conta += 1


class CaylaFala(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        # e o conteudo espera text como arguemnto que é passado na classe mensagem
        # se não for passado nada, terá texto vazio ''
        self.ids.lab.text = text


# Vai fazer mesma tarefa que a função Conteudo, mas com outra configurações
# Vai ser com balões invertido
class EuFala(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.meu.text = text


class PerdiTubes(App):
    def build(self):
        return Mensagem(['#euu oi', '#euu oii', '#cay oi', '#euu Você que comer algo?',
                         '#euu ?', '#cay Quero...'])


if __name__ == '__main__':
    PerdiTubes().run()
