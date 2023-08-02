# -*- coding: utf-8 -*-

from odoo import models, fields


class visit(models.Model):
    _name = 'test.visit'
    _description = 'visit'

    name = fields.Char(string = 'Descripcion')
    customer = fields.Char(string = 'Cliente')
    date = fields.Datetime(string = 'Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'Whatsapp'), ('T', 'Telefónico')], string='Tipo', required=True)
    done = fields.Boolean(string = 'Realizado')

