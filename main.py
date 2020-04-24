from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.metrics import sp
import os


'''
       Leia mais sobre o jogo no arquivo README.md
'''

# deixei como prevenção essa classe, caso eu erre
class Mensagem(BoxLayout):
    def __init__(self, mensagem, **kwargs):
        super().__init__(**kwargs)
        # A classe incial estará esperando a classe mensagem como argumento
        # Essa é aquela mensagem da lista da classe PerdiTubes
        self.mensagem = mensagem
        self.orientation = 'vertical'
        self.todas_mensagnes = len(mensagem)
        self.conta = 0
        self.tamanho = 0
        self.fala = []
        self.conversadas = []
        # Balões usados
        self.euu = 'img/balao_azul.png'
        # Váriavel usada para salvar o arquivo de texto
        self.primeira = True

        # Chama a mensagem a cada 4 segundo
        Clock.schedule_interval(self.chama_mensagem, 4)

    # Vai adicionar uma a uma as mensagens
    def chama_mensagem(self, sla):

        # Quando acabar as mensagens vai parar de adicionar os widgets, isso é para não dar erro.
        if self.conta < self.todas_mensagnes:
            # Nessa narrativa são duas pessoas, mas da para adicionar mais pessoas
            falas = {
                '@cay': CaylaFala(self.mensagem[self.conta][4:]),
                '@euu': EuFala(text=self.mensagem[self.conta][4:])
            }
            # Procura dentro da biblioteca quem está falando e adicina o widget
            self.ids.box.add_widget(falas[self.mensagem[self.conta][:4]])

            # Mostra a pessoa, se decomentar o [:4] mostra a conversa toda junto com a pessoa
            # print(self.mensagem[self.conta][:4])
            self.conta += 1

    def conversa_digitada(self):
        mifala = self.ids.mifala.text
        falas = {
            '@cay': CaylaFala(mifala[4:]),
            '@euu': EuFala(text=mifala[4:])
        }
        # Coloquei opção de adicionar fala digitada para me ajudar no roteiro da história
        
        self.ids.box.add_widget(falas[mifala[:4]])

        # Escrever no terminal a conversa que stá acontecendo
        print(mifala)
        self.conversadas.append(mifala)
        # Limpa o texto da caixa e deixa o @eeu, coloquei aqui o personagem que vai aparece mais, para facilitar
        self.ids.mifala.text = '@cay '

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


# # Cayla [Cayla + adiciona(balão)]
class CaylaFala(BoxLayout):
    def __init__(self, texto='', **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.cay = 'img/balao_rosa.png'
        self.padding=(10, 10, 0, 0)
        self.spacing = 10
        self.padding= (0, 20, 0, 10)
        self.add_widget(
            Button(
                size_hint = (None, None),
                pos_hint={'top':1.2},
                border=(0, 0, 0, 0),
                background_normal = 'img/personagens/cayla_rosa.png',
                background_down = 'img/personagens/cayla_rosa.png'
            ))
        # Balão adiciona balão da Cayla ao BoxLayout
        self.add_widget(Adaptavel(texto=texto, balao = self.cay))
        # Aqui vai ser preciso ser adicionado algo que identifique quantas letras
        # foi escrito e adicione o widget que melhor atende a situação


# Balão da Cayla
class Adaptavel(Button):
    def __init__(self, texto, balao, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.font_size = sp(30)
        self.text = texto
        self.pos_hint = {'bottom':1} 
        self.background_normal = balao
        self.background_down = balao
        

    def on_size(self, *args):
        self.text_size = (self.width - sp(30), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)
        self.width += sp(30)
        if self.width > 400:
            self.width = 400
        
        self.height = self.height



# Vai fazer mesma tarefa que a classe CaylaFala, mas com outra configurações e outras imagens e uma adaptação gambiarra
class EuFala(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.meu.text = text


# Personagem que está falando
class Personagem(Button):
    def __init__(self, person, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.border = (0, 0, 0, 0)
        self.background_normal = person
        self.background_down = person


# Label adapitavel
class Adapita(Label):
    def __init__(self, text= '', **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.font_size = sp(30)
        self.text = text

    def on_size(self, *args):
        self.text_size = (self.width - sp(10), None)

    def on_texture_size(self, *args):
        self.size = self.texture_size
        self.height += sp(20)

class PerdiTubes(App):
    def build(self):
        # Coloque @euu antes da frase para o balão ser adicionado ao seu lado + sua imagem
        # Ou coloque @cay antes para o balão ser adicionado do lado outra pessoa + a imagem da pessoa
        return Mensagem(['@cay ...', 
        '@cay Coisas que precisa ser feito',
        '@cay Comprar mascara',
        '@cay :)',
        '@cay isdhghgwghqhgawfajrfjwafjapojsfopajfosajfopssadjasd',
        '@euu Sim vc as vezes vc da uma pirada'])


if __name__ == '__main__':
    PerdiTubes().run()
