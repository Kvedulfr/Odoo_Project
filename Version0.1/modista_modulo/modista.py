#-*- encoding: utf-8 -*-
from odoo import time, models, fields, api

class modista_tienda(models.Model):
	#Nombre que vamos a usar para referirnos a nuestra clase en las vistas
	_name= 'modista.tienda'
	
	#Nombre de los atributos y con el atributo string le asignamos el valor "visual"
	nombre= fields.Char(string='Nombre Cliente', required=True)
	descripcion= fields.Text('Descripcion de Pedido', required=True)
	fecha= fields.Date(string='Fecha de pedido')
	t_pedido= fields.Selection(string='Tipo pedido',selection=[('1','Arreglo'),('2','Cofeccion a Medida'),('3','Traje Sevillana')], required=True)
	#Para poder agrupar despues y hacer el sumatorio del precio
	precio= fields.Float(string="Precio", group_operator="sum")
	telefono=fields.Char(string='Teléfono')
	pagado=fields.Boolean(string="¿Adelanto Pago?")
    #Enlace de los atributos de fields https://odoo-new-api-guide-line.readthedocs.io/en/latest/fields.html
	@api.multi 
	def limpiar_registros(self):
		self.nombre = ""
		self.descripcion = ""
		self.fecha = ""
		self.t_pedido = ""
		self.precio = 0
		#No se porque no me sale ¿No sería un valor por defecto?
		self.telefono = "+34"
		self.pagado = False

	def fecha_actual(self):
		self.fecha = time.strftime("%Y-%m-%d")

	
