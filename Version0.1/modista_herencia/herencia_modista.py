#-*- encoding: utf-8 -*-
from odoo import models, fields, api
class HerenciaModel(models.Model):
    #Herencia del modulo modista.tienda
    _name = 'herencia.model'
    _inherit ='modista.tienda'
    user_id = fields.Many2one('res.users', 'Responsible')
    prueba= fields.Char(string='Prueba')
    fecha2= fields.Date(string='Fecha de Pago')
    

    @api.multi    
    def limpiar_registros(self):
        self.user_id = ""
        self.prueba = ""
        self.fecha2 = ""
		
   