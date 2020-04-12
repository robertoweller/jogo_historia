from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from functools import partial
from kivy.uix.scatter import ScatterPlane

class Adicionar(App):
	def escreve(self, cont, c):
		if cont == 'Novo floatlayout':
			self.flat.append(self.ad)
			print('tentou adicionar?')
			for i in self.flat:
				#Adiciona um float
				btt = Button(text = i, size_hint = (.5, .10), pos = (293, 370))
				escala = ScatterPlane()
				self.ftt.add_widget(btt)
				btt.bind(on_release=partial(self.escreve, i))
		
		if cont == '+':
			print('pegadinha do malandro')
			# Adiciona um elemento a tabela necessarios self.ad = '0'
			self.necessarios.append(self.ad)
			if cont in self.necessarios:
				self.necessarios.remove('Novo floatlayout')
				self.necessarios.remove('Atualiza')
				self.necessarios.remove('Dinheiro')
				self.necessarios.remove('+')
				print('apagou')
			for i in self.necessarios:
				bt = Button(text = i, size_hint = (.5, .10), pos = (20, 20))
				self.bx.add_widget(bt)
				bt.bind(on_release=partial(self.escreve, i))
			
		if '0' in self.necessarios:
			self.necessarios.remove('0')
		if '0' in self.flat:
			self.flat.remove('0')
	def build(self):
		self.ad = '0'
		self.ft = FloatLayout()
		self.ftt = FloatLayout()
		self.bx = BoxLayout()
		self.necessarios = ['Novo floatlayout', 'Atualiza', 'Dinheiro', '+']
		self.flat = []
		for i in self.necessarios:
			bt = Button(text = i, size_hint = (.5, .10), pos = (20, 20))
			self.bx.add_widget(bt)
			bt.bind(on_release=partial(self.escreve, i))
			
		self.ft.add_widget(self.bx)
		self.ft.add_widget(self.ftt)	
		return self.ft
		
		
		
Adicionar().run()


