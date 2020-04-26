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
        # Variáveis importantes para rodar o jogo
        self.mensagem = mensagem
        self.orientation = 'vertical'
        self.todas_mensagnes = len(mensagem)
        self.conta = 0
        self.tamanho = 0
        # Aqui dica as conversas que é salva no documento conversa.txt
        self.conversadas = []

        # Balões usados
        self.euu_balao = 'img/baloes/eu_baixo.png'
        self.cay_balao = 'img/baloes/cay_baixo.png'
        # Personagens
        self.cayla = 'img/personagens/cayla_rosa.png'
        self.eu_modelo = 'img/personagens/modelo.png'

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
                '@cay': PersonFala(
                    eu=False,
                    texto = self.mensagem[self.conta][4:], 
                    balao = self.cay_balao,
                    person = self.cayla
                    ),
                '@euu': PersonFala(
                    eu=True,
                    texto=self.mensagem[self.conta][4:],
                    balao=self.euu_balao,
                    person= self.eu_modelo)
            }

            # Procura dentro da biblioteca quem está falando e adicina o widget
            self.ids.box.add_widget(falas[self.mensagem[self.conta][:4]])

            # Mostra a pessoa que está falando
            # print(self.mensagem[self.conta][:4])
            
            self.conta += 1

    def conversa_digitada(self):
        mifala = self.ids.mifala.text
        falas = {
            '@cay': PersonFala(
                eu=False,
                texto = mifala[4:], 
                balao = self.cay_balao,
                person=self.cayla
                
                ),
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


# # Personagem [Person + adiciona(balão)]
class PersonFala(BoxLayout):

    def __init__(self, texto='', balao='', person='', eu=False, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.balao = balao
        self.person = person

        # Espaçamento do topo e de baixo
        self.padding=(0, 10, 0, 10)
        # Espaçamento entre o o personagem e o balão
        self.spacing = 15
        # Ajuste da posiçao da imagem
        self.centro = 1
        if eu:
            self.add_widget(Adaptavel(
                texto=texto, 
                balao = self.balao
                ))
            self.add_widget(Button(
                    size_hint = (None, None),
                    pos_hint = {'center':self.centro},
                    border = (0, 0, 0, 0),
                    background_normal = self.person,
                    background_down= self.person
            ))    

        else:
            self.add_widget(
                # Personagem que vai aparecer
                Button(
                    size_hint = (None, None),
                    pos_hint={'center': self.centro},
                    border=(0, 0, 0, 0),
                    background_normal = self.person,
                    background_down = self.person
                ))
            # Balão adicionado ao BoxLayout
            self.add_widget(Adaptavel(texto=texto, balao = self.balao))
            # Adicione um widget que melhor atenda a situação


# Classe dos balões
class Adaptavel(Button):
    def __init__(self, texto, balao, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.font_size = sp(30)
        self.text = texto
        # Vai tentar deixar o balão sempre mais abaixo possivel
        self.pos_hint = {'bottom':1} 
        # Fundo do balão
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



# Vai fazer mesma tarefa que a classe PersonFala, mas com outra configurações e outras imagens e uma adaptação gambiarra
class EuFala(BoxLayout):
    def __init__(self, text='', **kwargs):
        super().__init__(**kwargs)
        self.ids.meu.text = text



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
        """
        Coloque @euu ou @cay antes da frase para passar para para classe mensagem
        qual personagem está falando, então o personagem é adicionado a conversa
        """
        return Mensagem(['@cay ...', 
        '@cay Coisas que precisa ser feito',
        '@cay Comprar mascara',
        '@cay :)',
        '@cay isdhghgwghqhgawfajrfjwafjapojsfopajfosajfopssadjasd',
        '@euu Sim vc as vezes vc da uma pirada'])


if __name__ == '__main__':
    PerdiTubes().run()
