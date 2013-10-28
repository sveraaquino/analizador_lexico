#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygraphviz as pgv
import re
from xml.dom.minidom import parse

class  graficoAutomata:

	document = None
	nodes = {}
	
	def __init__(self, svg_file_name) :
		
		self.svg_file_name = svg_file_name
	
	
	
	def load_nodes(self) :

		self.document = parse(self.svg_file_name)
		self.document.normalize()
		self.elements = self.document.documentElement
		self.polygons = []
		#se obtiene del svg todos los elementos  que contienen el tag
		#<g> ... </g>
		for polygon in self.elements.getElementsByTagName("g") :
			#se procesan unicamente aquellos tags que son del tipo nodo
			if polygon.attributes["class"].value == "node" :
				#se obiene el tag <title>.. </title>
				title = polygon.getElementsByTagName("title")[0]
				#se verifica si el tag posee un valor
				if title.firstChild !=  None:
					#se obtiene el valor contenido dentro del tag
					label = str(title.firstChild.data).strip()
					#se obtiene el tag <ellipse>... </ellipse>
					ellipse = polygon.getElementsByTagName("ellipse")[0]
					self.polygons.append(ellipse)
					#se guarda en el diccionario el id del estado y la
					#referencia a la figura
					# ["E4"] -> <ellipse fill="none" stroke="black"/>
					#print ellipse
					self.nodes[label] = ellipse#len(self.polygons)-1
	
	def set_node_color(self, node_id, color="#ADD8E6") :
		#print node_id
		if self.nodes.has_key(node_id) :
			self.nodes[node_id].attributes["fill"].value = color
	
			#print  node_id + "->" +  self.nodes[node_id].attributes["fill"].value
	
	
	def write_svg(self, svg_file_name=None) :

		if svg_file_name == None :
			svg_file_name =  self.svg_file_name
		#se el archivo, si no existe se crea
		source = open(svg_file_name, 'w+')
		# se escribe en el archivo el contenido del documento xml actual
		ugly = self.document.toxml()
		source.write(ugly)
		#se cierra el archivo
		source.close()
	
	def gen_svg_from_automata(self, automata, layout_prog="dot") :

		#se crea un grafo dirigido
		gr = pgv.AGraph(directed=True,rankdir="LR", strict=False)
		estados = {}
		inicio = automata.estado_inicial
		#se otienen todos los estados del dict
		estado_list = [] + automata.estados.values()
		#se ordenan los estados
		estado_list.sort()
	
		for estado in estado_list :
			if estado.final :
				#si es un estado final se añade con un doble circulo
				gr.add_node(estado.id, shape = "doublecircle")
			else :
				#si no es un estado final se añade con un circulo
				gr.add_node(estado.id, shape = "circle")
	
		#Se añade un nodo "invisible"
		gr.add_node(u"\u2205",width="0",height="0")
		#se añade un arcon entre el nodo vacio y el estado inicial del
		#automata, con esto se obtiene el siguiente grafico :
		# --Inicio--> (Estado Inicial)
		gr.add_edge((u"\u2205",inicio.id), label="Inicio", color='#8dad48')
		#por cada arco definido se añade las relaciones entre los nodos
		#definidos anteriormente
		for arco in automata.arcos :
			#se añaden los arcos entre los estados y el simbolo de
			#de transicion, con esto se consigue un lo siguiente :
			print '(inicio) ---simbolo --->(destino)'
			gr.add_edge((arco.origen.id.decode("utf-8"),arco.destino.id.decode("utf-8")),label=arco.simbolo.decode("utf-8"),color='#8dad48')
	
		#se utiliza el agoritmo dot para el grafo
		#neato|dot|twopi|circo|fdp
		gr.layout(prog=layout_prog)
		#se escribe el grafo resultado en un archivo
		gr.draw(self.svg_file_name)
	
	
