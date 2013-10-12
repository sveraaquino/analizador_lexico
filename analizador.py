class analizador:
	def __init__(self,alfabeto,expresion):
		self.alfabeto = alfabeto
		self.expresion = expresion
		self.operUnario = '+*?'
		self.operadores = '+*?.|'
		self.indice = 0
		
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
		print "aquiiiiiii -> Token = ", self.expresion[self.indice]
		self.subTerm()
		
		
	def factor(self):
		print "factor -> Token = ", self.expresion[self.indice]
		
		if self.expresion[self.indice] in self.alfabeto:
			print "alfabeto -> Token = ", self.expresion[self.indice]
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
			if (self.indice+1)<len(self.expresion):
				self.indice = self.indice+1
			
			
	def subExpr(self):
		
		if self.expresion[self.indice] != '|':
			return
		
		print "operadorBinaria -> Token = |"
		self.indice = self.indice+1
		self.term()
		self.subExpr()
		
		
	def subTerm(self):
		if self.expresion[self.indice] != '.':
			return
		
		print "operadorBinaria -> Token = ."
		self.indice = self.indice+1
		self.factor()
		self.subTerm()
		
		
alfa=raw_input('Introduzca el alfabeto:')
expre=raw_input('Introduzca la expresion regular:')
defi= analizador(alfa,expre)
defi.validar_expresion()
		
	
