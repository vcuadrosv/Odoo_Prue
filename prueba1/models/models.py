# -*- coding: utf-8 -*-

from odoo import models, fields


class ficha_empleados(models.Model):
    _name = 'ficha.empleados'
    _description = 'empleados'


    STATE_SELECTION = [
        ('activo', 'Activo'),
        ('no_activo', 'No Activo'),
    ]

    SEX_SELECTION = [
        ('masculino', 'Masculino'),
        ('femenino', 'Femenino'),
        ('otro', 'Otro'),
    ]

    JOR_SELECTION = [
        ('Jornada_Completa', 'Jornada Completa'),
        ('Media_Jornada', 'Media_Jornada'),
        ('No_tiene', 'No tiene'),
    ]

    Foto = fields.Image(required=True)
    nombre = fields.Char (string = 'Primer Nombre', required=True)
    nombre2 = fields.Char (string = 'Segundo Nombre')
    apellido = fields.Char (string = 'Primer Apellido',required=True)
    apellido2 = fields.Char (string = 'Segundo Apellido')
    tipo = fields.Selection([('CC', 'Cedula de Ciudadania'), ('NIT', 'Numero de identificacion tributaria'), ('RC', 'Registro Civil'),
                            ('TI', 'Tarjeta de Identidad'),('CE', 'Cedula de extranjeria'),('PA', 'Pasaporte')], string='Tipo', required=True, help="Seleccione el tipo de documento:\n"
                                                                                                                                                    "- CC: Cedula de Ciudadania\n"
                                                                                                                                                    "- NIT: Numero de identificacion tributaria\n"
                                                                                                                                                    "- RC: Registro Civil\n"
                                                                                                                                                    "- TI: Tarjeta de Identidad\n"
                                                                                                                                                    "- CE: Cedula de extranjeria\n"
                                                                                                                                                    "- PA: Pasaporte")
    numero_cedula = fields.Char(string="Número de Cédula")
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    cargo = fields.Char (string = 'Cargo')
    celular = fields.Integer(string="Celular")
    direccion = fields.Char(string='Dirección', required=True)
    tipo_sangre = fields.Char(string='Tipo de Sangre')
    email = fields.Char(string='Correo electrónico', required=True)
    estado = fields.Selection(STATE_SELECTION, string='Estado', default='activo', required=True)
    sexo = fields.Selection(SEX_SELECTION, string='Sexo', required=True)
    jornada = fields.Selection(JOR_SELECTION, string='Jornada', required=True)



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

