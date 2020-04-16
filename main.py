from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import os
'''
       Leia mais sobre o jogo no arquivo README.md
'''


class Mensagem(BoxLayout):
    def __init__(self, mensagem, **kwargs):
        super().__init__(**kwargs)
        # A classe incial estará esperando a classe mensagem como argumento
        # Essa é aquela mensagem da lista da classe PerdiTubes
        self.mensagem = mensagem
        self.todas_mensagnes = len(mensagem)
        self.conta = 0
        self.fala = []
        self.conversadas = []
        self.primeira = True

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
                '@cay': CaylaFala(text=self.mensagem[self.conta][4:]),
                '@euu': EuFala(text=self.mensagem[self.conta][4:])
            }

            # Procura dentro da biblioteca quem está falando e adicina o widget
            self.ids.men.add_widget(falas[self.mensagem[self.conta][:4]])

            # Mostra a pessoa, se decomentar o [:4] mostra a conversa toda junto com a pessoa
            # print(self.mensagem[self.conta][:4])
            self.conta += 1

    def conversa_digitada(self):
        mifala = self.ids.mifala.text
        falas = {
            '@cay': CaylaFala(text=mifala[4:]),
            '@euu': EuFala(text=mifala[4:])
        }
        # Coloquei opção de adicionar fala digitada para me ajudar no roteiro da história
        self.ids.men.add_widget(falas[mifala[:4]])

        # Escrever no terminal a conversa que stá acontecendo
        print(mifala)
        self.conversadas.append(mifala)
        # Limpa o texto da caixa e deixa o @eeu, coloquei aqui o personagem que vai aparece mais, para facilitar
        self.ids.mifala.text = '@euu '

    def salva(self):
        if self.primeira:
            print(f'{self.mensagem}')
            cov = f'{self.mensagem}'
            if str(self.mensagem) != '[]':
                # Mensagem salva no documento conversas.txt
                os.system(f'echo "{cov}" > conversas.txt')
            if str(self.conversadas) != '[]':
                # print(self.conversadas)
                cov = f'{self.mensagem}\n{self.conversadas}'
                os.system(f'echo "{cov}" > conversas.txt')
            self.primeira = False
        else:
            if str(self.conversadas) != '[]':
                cov = f'{self.mensagem}\n{self.conversadas}'
                os.system(f'echo "{cov}" > conversas.txt')
                # print(self.conversadas)


class CaylaFala(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        # e o conteudo espera text como arguemento que é passado na classe mensagem
        # se não for passado nada, terá texto vazio ''
        self.ids.lab.text = text


# Vai fazer mesma tarefa que a classe CaylaFala, mas com outra configurações e outras imagens
class EuFala(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.meu.text = text


class PerdiTubes(App):
    def build(self):
        # Coloque @euu antes da frase para o balão ser adicionado ao seu lado + sua imagem
        # Ou coloque @cay antes para o balão ser adicionado do lado outra pessoa + a imagem da pessoa
        return Mensagem(['@cay oi hihi', '@euu olá :)'])


if __name__ == '__main__':
    PerdiTubes().run()
