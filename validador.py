#! /usr/bin/env python
# -*- coding: utf-8 -*-


from minimo import TablaTransiciones




class validadorAFD :
    
	def __init__(self, afd, secuencia_caracteres):


		self.afd =  afd		
		#se construye la tabla de transiciones apartir del afd
		self.tabla_transiciones = TablaTransiciones(afd)
		self.tabla_transiciones.build_table()
		#estados que representaran las transiciones
		self.estado_origen = self.afd.get_estado_inicial()
		self.estado_destino = None
		self.estado_anterior = {}
		#el indice del caracter acualtmente procesado
		self.simbol_index = -1
		self.secuencia_caracteres = secuencia_caracteres
	
	def next_state(self): 

		#si es el estado inicial se pinta unicamente ese estado
		if self.simbol_index == -1 :
			self.simbol_index += 1
			#print self.estado_origen
			
		elif self.simbol_index  >= 0 and \
			self.simbol_index < len(self.secuencia_caracteres): 
			
			self.__next_state()
		else :
			print '=========================',self.estado_origen.id
			
			if self.estado_origen.final:
				print 'La cadena pertenece al lenguaje'
			else:
				print 'La cadena no pertenece al lenguaje'
			return False
		
		return True
	
			
	def __next_state(self):  

		#se obiente el siguiente caracter
		caracter = self.secuencia_caracteres[self.simbol_index]
		print '=========================',self.estado_origen.id
		#se establece el estado anterior
		self.estado_anterior[str(self.simbol_index)] =  self.estado_origen
		#se obiene el estado destino resultante de la transicion 
		#producida por el simbolo caracter del estado origen
		id = self.estado_origen.id + caracter
		self.estado_destino = self.tabla_transiciones.get_table_value(id)
		#si el estado destino es None ocurrio un error
		if self.estado_destino != None :
			#el estado origen pasa a ser el estado actualmente procesado
			#el estado destino
			self.estado_origen = self.estado_destino
		else :
			print 'error no se puede continuar la validacion'
		
		self.simbol_index+=1
		



