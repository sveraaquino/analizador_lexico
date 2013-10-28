#! /usr/bin/env python
# -*- coding: utf-8 -*-

from automata import *


class codigo:


	def __init__(self, afd):
		self.afd=afd
		
	def imprimir(self):
		
		print 'class afd:'
		print '\tdef __init__(self,cadena):'
		print '\t\tself.cadena=cadena'
		
		print '\tdef validar(self):'
		print '\t\testado = '+self.afd.get_estado_inicial().get_id()
		print '\t\tfor c in self.cadena:'
		print '\t\t\testado = estadoSiguiente(estado,c)'
		print '\t\t\tif estado = -1:'
		print '\t\t\t\tprint \'La cadena no pertenece al lenguaje\''
		print '\t\t\t\texit()'
		
		
		finales={}
		estados={}
		for estate in self.afd.get_arcos():
			if estate.get_origen().get_final():
				indice = estate.get_origen().get_id()
				finales[indice]=indice
			indice = estate.get_origen().get_id()
			estados[indice]=indice
		
		
		for estate in finales:
				print '\t\t\tif estado = '+estate+':'
				print '\t\t\t\tprint \'La cadena pertenece al lenguaje\''
		
		print '\t\t\telse:'
		print '\t\t\t\tprint \'No finaliza en un estado final\''
		
		print '\tdef __estadoSiguiente(self,estado,caracter):'
		print '\t\tswitch(estado):'
		for estate in estados:
			print '\t\t\tcase('+estate+'):'
			print '\t\t\t\tswitch(caracter):'
			for arcos in self.afd.get_arcos():
				if estate == arcos.get_origen().get_id():
					print '\t\t\t\t\tcase('+arcos.get_simbolo()+'):'
					print '\t\t\t\t\t\treturn '+arcos.get_destino().get_id()
					
			print '\t\t\t\tdefault:'
			print '\t\t\t\t\treturn -1'
		
		print 'return 0'			
					
					
		
		
		
		print 'cadena=raw_input(\'Introduzca la cadena a validar:\')'
		print 'afd = afd(cadena)'
		print 'afd.validar()'
