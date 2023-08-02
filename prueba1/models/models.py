# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.exceptions import UserError

class Visit(models.Model):
    _name = 'prueba1.visit'
    _description = 'Visit'
    def custom_button_action(self):
        self.done = not  self.done
    #boton donde se marca en el views
    name = fields.Char(string='Descripción')
    customer = fields.Char(string='Cliente')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'Whatsapp'), ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string='Realizado')
    imagen = fields.Image(string="Imagen")
    auto = fields.Many2one('fabricante.vehiculo', string='Tipo de Auto', required=True, display_name='marca', domain="[('marca', '!=', False)]")
    #display_name='marca', domain="[('marca', '!=', False)]"
                        
class FabricanteVehiculo(models.Model):
    _name = 'fabricante.vehiculo'
    _description = 'Fabricante de Vehículos'
    _order = 'marca'  # Ordenar alfabéticamente la marca de vehículos
    _rec_name = 'marca'
    marca = fields.Char(string='Marca', required=True)
    imagen = fields.Binary(string='Imagen')

