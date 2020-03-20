#-*- encoding: utf-8 -*-
from odoo import time, models, fields, api
#Import para controlar Validar los campos
from odoo.exceptions import UserError, AccessError, ValidationError

class cliente(models.Model):
	#Nombre que vamos a usar para referirnos a nuestra clase en las vistas
	_name= 'modista.cliente'
	#Sirve para indicar que campo se va a visualizar en el menu de many2one (display)
	_rec_name='nombre'
	_sql_constraints = [
    	  ('telefono_unique',
         'unique(telefono)',
         "El telefono ya existe, comprueba que el cliente no lo haya insertado antes.")]
	
	#Nombre de los atributos y con el atributo string le asignamos el valor "visual"
	nombre= fields.Char(string='Nombre Cliente', required=True)
	telefono=fields.Integer(string='Teléfono',required=True, help="Si no te dan telefono puedes ponerlo en 0")
	
    #Enlace de los atributos de fields https://odoo-new-api-guide-line.readthedocs.io/en/latest/fields.html
	@api.multi 
	def limpiar_registros(self):
		self.nombre = ""		
		self.telefono = ""

	#Funcion para comprobar que el campo es correcto
	@api.constrains('telefono')
	def _check_number(self):
	  telefono = self.telefono
	  if telefono and len(str(abs(telefono))) != 9:
		  raise ValidationError('Has insertado un numero de telefono invalido tiene: '+telefono)
	




class pedido(models.Model):
	#Nombre que vamos a usar para referirnos a nuestra clase en las vistas
	_name= 'modista.pedido'
	_sql_constraints = [
    	  ('fecha_pago_check',
         'CHECK(fecha_pago >= fecha_p)',
         "La fecha de pago no puede ser menor que del pedido"),
		 ('fecha_r_check',
         'CHECK(fecha_r >= fecha_p)',
         "La fecha de recogida no puede ser menor que del pedido")]
	
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
		#self.t_pedido = ""
		self.fecha_pago = ""
		self.fecha_p = ""
		self.fecha_r = ""
		self.precio = 0
		self.descripcion = ""
		#self.cliente=""

	#Funcion para comprobar que el campo es correcto
	@api.constrains('precio')
	def _check_price(self):
	  if self.precio < 0:
		  raise ValidationError('Has insertado un valor negativo por lo tanto no es valido')	  
	  	
		
	def fecha_actual(self):
		self.fecha = time.strftime("%Y-%m-%d")
