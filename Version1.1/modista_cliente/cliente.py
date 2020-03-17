#-*- encoding: utf-8 -*-
from odoo import time, models, fields, api

class cliente(models.Model):
	#Nombre que vamos a usar para referirnos a nuestra clase en las vistas
	_name= 'modista.cliente'
	#Sirver para indicar que campo se va a visualizar en el menu de many2one (display)
	_rec_name='nombre'
	
	#Nombre de los atributos y con el atributo string le asignamos el valor "visual"
	nombre= fields.Char(string='Nombre Cliente', required=True)
	telefono=fields.Char(string='Teléfono',required=True)
	
    #Enlace de los atributos de fields https://odoo-new-api-guide-line.readthedocs.io/en/latest/fields.html
	@api.multi 
	def limpiar_registros(self):
		self.nombre = ""		
		self.telefono = "+34"
		

