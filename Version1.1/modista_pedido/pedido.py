#-*- encoding: utf-8 -*-
from odoo import time, models, fields, api

class pedido(models.Model):
	#Nombre que vamos a usar para referirnos a nuestra clase en las vistas
	_name= 'modista.pedido'
	
	t_pedido= fields.Selection(string='Tipo pedido',selection=[('1','Arreglo'),('2','Cofeccion a Medida'),('3','Traje Sevillana')], required=True)
	fecha_p= fields.Date(string='Fecha de pedido')
	fecha_pago= fields.Date(string='Fecha de pago')
	fecha_r= fields.Date(string='Fecha de recogida')
	pagado=fields.Boolean(string='¿Pagado?')
	#cliente=fields.Many2one("modista.cliente",string="Cliente")
	cliente=fields.Many2one('modista.cliente','Cliente',required="true")
	precio= fields.Float(string="Precio", group_operator="sum")
	descripcion= fields.Text('Descripcion de Pedido', required=True)
	
	
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
		
	def fecha_actual(self):
		self.fecha = time.strftime("%Y-%m-%d")