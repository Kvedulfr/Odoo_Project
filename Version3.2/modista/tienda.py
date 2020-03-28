#-*- encoding: utf-8 -*-
from odoo import time, models, fields, api 
#Import para controlar Validar los campos
from odoo.exceptions import UserError, AccessError, ValidationError
#Import para hacer la expresiones regulares
import re

class cliente(models.Model):
	#Nombre que vamos a usar para referirnos a nuestra clase en las vistas
	_name= 'modista.cliente'
	#Sirve para indicar que campo se va a visualizar en el menu de many2one (display)
	_rec_name='nombre'
	''' Eliminado restriccion unica
	_sql_constraints = [
    	  ('telefono_unique',
         'unique(telefono)',
         "El teléfono ya existe, comprueba que el cliente no lo hayas insertado antes.")]
		 '''
		 #Para evitar que inserte el mismo nombre.
	_sql_constraints = [
    	  ('nombre_unique',
         'unique(nombre)',
         "El nombre ya existe, comprueba que el cliente no lo hayas insertado antes.")]	 
	
	#Nombre de los atributos y con el atributo string le asignamos el valor "visual"
	nombre= fields.Char(string='Nombre Cliente', required=True)
	
	#telefono=fields.Integer(string='Teléfono',required=True, help="Si no te dan telefono puedes ponerlo en 0")
	telefono=fields.Char(string='Teléfono',required=True, help="El formato válido es del tipo = 123-456-789.")
	pedido=fields.One2many('modista.pedido','cliente','Pedidos del cliente')
	
    #Enlace de los atributos de fields https://odoo-new-api-guide-line.readthedocs.io/en/latest/fields.html
	@api.multi 
	def limpiar_registros(self):
		self.nombre = ""		
		self.telefono = "0"

	#Funcion para comprobar que el campo es correcto (Tomando el telefono como tipo Integer)
	"""
	@api.constrains('telefono')
	def _check_number(self):
	  telefono = self.telefono
	  if telefono and len(str(abs(telefono))) != 9:
		  raise ValidationError('Has insertado un número de teléfono inválido tiene: '+teléfono)
	
	"""
	#Funcion para comprobar que no se inserte un nombre en blanco o un caracter espacio al principio
	@api.constrains('nombre')
	def _chek_name(self):
		if re.search("^\s", self.nombre)!= None:
			raise ValidationError('Has colocado un espacio al principio del nombre o no has insertado ningun nombre.')

	#Funcion para comprobar que el campo es correcto (Tomando el telefono como tipo Integer)
	@api.constrains('telefono')
	def _check_number(self):
		if self.telefono != "0":
			if re.search("^[0-9]{3}-{1}?[0-9]{3}-{1}?[0-9]{3}$", self.telefono) == None:
				raise ValidationError('Has insertado un teléfono invalido. \n El único formato válido es del tipo'\
									' 123-456-789 o 0 si no tienes numero de teléfono')	
"""			#No va por problemas de logica
		if (re.search("^[0-9]{3}-{1}?[0-9]{3}-{1}?[0-9]{3}$", self.telefono) == None or self.telefono == "0"):
			raise ValidationError('Has insertado un teléfono invalido. \n El único formato válido es del tipo'\
									' 123-456-789 o 0')		
"""

class pedido(models.Model):
	#Nombre que vamos a usar para referirnos a nuestra clase en las vistas
	_name= 'modista.pedido'
	_sql_constraints = [
    	  ('fecha_pago_check',
         'CHECK(fecha_pago >= fecha_p)',
         "La fecha de pago no puede ser menor que del pedido."),
		 ('fecha_r_check',
         'CHECK(fecha_r >= fecha_p)',
         "La fecha de recogida no puede ser menor que del pedido.")]
	
	t_pedido= fields.Selection(string='Tipo pedido',selection=[('1','Arreglo'),('2','Cofeccion a Medida'),('3','Traje Sevillana')], required=True)
	fecha_p= fields.Date(string='Fecha de pedido',required=True)
	fecha_pago= fields.Date(string='Fecha de pago')
	fecha_r= fields.Date(string='Fecha de recogida')
	pagado=fields.Selection(string='¿Pagado?',selection=[('1','Pagado'),('2','No Pagado')], required=True)
	#pagado=fields.Boolean(string='¿Pagado?')
	#cliente=fields.Many2one("modista.cliente",string="Cliente")
	cliente=fields.Many2one('modista.cliente','Cliente',required="true")
	precio= fields.Float(string="Precio",  group_operator="sum")
	descripcion= fields.Text('Descripcion de Pedido', required=True)
	image= fields.Binary('Imagen')
	
	
	
    #Enlace de los atributos de fields https://odoo-new-api-guide-line.readthedocs.io/en/latest/fields.html
	@api.multi 
	def limpiar_registros(self): #Atributos comentados no pueden ser nulos
		
		self.fecha_pago = False #Con el false indicamos que queden vacios
		self.fecha_p = time.strftime("%Y-%m-%d")
		self.fecha_r = False
		self.precio = 0
		self.descripcion = ""
		#self.cliente=""

	#Funcion para comprobar que el campo es correcto
	@api.constrains('precio')
	def _check_price(self):
	  if self.precio < 0:
		  raise ValidationError('Has insertado un PRECIO NEGATIVO por lo tanto no es valido')	  
	
	@api.constrains('fecha_pago')
	def _chech_paydate(self):
		#Si el campo es vacio python lo reconoce como falso
		if self.pagado == '2' and self.fecha_pago != False :
			raise ValidationError('El producto NO esta PAGADO por lo tanto no puedes insertar una FECHA DE PAGO ')

	@api.constrains('fecha_r')
	def _chech_paydate(self):
		#Si el campo es vacio python lo reconoce como falso
		if self.fecha_r != False:
			if self.fecha_r < self.fecha_p :
				raise ValidationError('No se puede RECOGER un pedido antes de la FECHA DE RECOGIDA')


		
	def fecha_actual(self): #No le doy uso
		self.fecha = time.strftime("%Y-%m-%d")

class gastos(models.Model):
	_name= 'modista.gastos'
	nombre_p=fields.Char(string="Producto", required=True)
	cantidad=fields.Integer(string="Cantidad",required=True)
	coste=fields.Float(string="Precio", group_operator="sum")
	descripcion=fields.Text(string="Comentario")
	fecha_c=fields.Date(string="Fecha de compra")

	#Boton para limpiar el registro
	@api.multi 
	def limpiar_registros(self): #Atributos comentados no pueden ser nulos
		#self.t_pedido = ""
		self.nombre_p = ""
		self.cantidad = 0
		self.coste = 0
		self.fecha_c = False
		self.descripcion = ""
		
	
	#Comprobamos que el coste no es negativa
	@api.constrains("coste")
	def _check_coste(self):
		if self.coste < 0:
			raise ValidationError("No se puede insertar un coste negativa")

	#Comprobamos que no se pueda insertar una cantidad negativa
	@api.constrains('cantidad')
	def _check_stock(self):
		if self.cantidad < 0:
			raise ValidationError('No puedes insertar una cantidad negativa')

