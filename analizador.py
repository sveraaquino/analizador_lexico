#! /usr/bin/env python
# -*- coding: utf-8 -*-

from thompson import *
from subconjunto import *
from minimo import *
from validador import *
from codigo import *
from grafico import *

class analizador:
	def __init__(self,alfabeto,expresion):
		self.alfabeto = alfabeto
		self.expresion = expresion
		self.operUnario = '+*?'
		self.operadores = '+*?.|'
		self.indice = 0
		self.postfija=[]
		
	def check_expresion(self):
		leng=len(self.expresion)
		
		for posicion in range(leng):
			
			"""print self.expresion[posicion]"""
			if not(self.expresion[posicion] in self.alfabeto or self.expresion[posicion] in self.operadores or self.expresion[posicion]=='(' or self.expresion[posicion]==')'):
				return False
				
		
		return True
		
		
	"""Funcion que valida la expresion regular introducida (BNF)"""			
	def validar_expresion(self):
		if self.check_expresion():
			self.expr()	
			print 'Expresion regular correcta'
			print 'Postfija',self.postfija
		else:
			print 'La expresion regular no esta contenida en el alfabeto de entrada'
	
	"""Componente del BNF, expresion de inicio"""
	def expr(self):
		
		print "exp -> Token = ", self.expresion[self.indice]
		self.term()
		self.subExpr()
		
	def term (self):
		
		print "term -> Token = ", self.expresion[self.indice]
		self.factor()
		self.subTerm()
		
		
	def factor(self):
		print "factor -> Token = ", self.expresion[self.indice]
		
		if self.expresion[self.indice] in self.alfabeto:
			print "alfabeto -> Token = ", self.expresion[self.indice]
			self.postfija.append(self.expresion[self.indice])
			if (self.indice+1)<len(self.expresion):
				self.indice = self.indice+1
			
		elif self.expresion[self.indice] == '(':
			print "Parentesis Abierto -> Token = ("
			self.indice = self.indice+1
			self.expr()
			
			if self.expresion[self.indice] != ')':
				print 'Error de sintaxis, se esperaba: )'
				exit()
			print "Parentesis Cerrado -> Token = )"
			if (self.indice+1)<len(self.expresion):
				self.indice = self.indice+1
			
		if self.expresion[self.indice] in self.operUnario:
			print "operacionUnaria -> Token = ", self.expresion[self.indice]
			self.postfija.append(self.expresion[self.indice])
			if (self.indice+1)<len(self.expresion):
				self.indice = self.indice+1
			
			
	def subExpr(self):
		
		if self.expresion[self.indice] != '|':
			return
		
		print "operadorBinaria -> Token = |"
		
		self.indice = self.indice+1
		self.term()
		self.postfija.append('|')
		self.subExpr()
		
		
	def subTerm(self):
		if self.expresion[self.indice] != '.':
			return
		
		print "operadorBinaria -> Token = ."
		self.indice = self.indice+1
		self.factor()
		self.postfija.append('.')
		self.subTerm()
		
		
alfa=raw_input('Introduzca el alfabeto:')
expre=raw_input('Introduzca la expresion regular:')
defi= analizador(alfa,expre)
defi.validar_expresion()

thomp = Thompson(defi.postfija)
afn = thomp.start()
subconj = Subconjuntos(afn,defi.alfabeto)
afd=subconj.start_subconjutos()
opMinimo = AFD(afd)
minimo = opMinimo.minimizar()

secuencia=raw_input('Introduzca la secuencia de caracteres:')
afd2 = validadorAFD(minimo, secuencia)

while afd2.next_state():
	a=1
	
generate = codigo(minimo)
generate.imprimir()

svg = graficoAutomata('images/afn.svg')
svg.gen_svg_from_automata(afn)
svg = graficoAutomata('images/afd.svg')
svg.gen_svg_from_automata(afd)
svg = graficoAutomata('images/afdm.svg')
svg.gen_svg_from_automata(minimo)
	



		
	
