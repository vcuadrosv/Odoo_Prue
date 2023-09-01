# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta


class ficha_empleados(models.Model):
    _name = 'ficha.empleados'
    _description = 'empleados'
    _rec_name = 'nombre'



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

    Foto = fields.Image (string = "Logo", max_width=128, max_height=128, required=True)
    nombre = fields.Char (string = 'Nombres completos', required=True)
    apellido = fields.Char (string = 'Apellidos completos',required=True)
    tipo = fields.Selection([('Cedula de Ciudadania','CC'), ('Numero de identificacion tributaria','NIT'), ( 'Registro Civil','RC'),
                            ( 'Tarjeta de Identidad', 'TI'),('Cedula de extranjeria','CE'),('Pasaporte','PA')], string='Tipo de documento', required=True, help="Seleccione el tipo de documento:\n"
                                                                                                                                                    "- CC: Cedula de Ciudadania\n"
                                                                                                                                                    "- NIT: Numero de identificacion tributaria\n"
                                                                                                                                                    "- RC: Registro Civil\n"
                                                                                                                                                    "- TI: Tarjeta de Identidad\n"
                                                                                                                                                    "- CE: Cedula de extranjeria\n"
                                                                                                                                                    "- PA: Pasaporte")
    numero_cedula = fields.Char(string="Número de cédula")
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento', required=True)
    cargo = fields.Char (string = 'Cargo empresarial')
    celular = fields.Integer(string="Numero de celular")
    direccion = fields.Char(string='Dirección de residencia', required=True)
    tipo_sangre = fields.Selection([('A+', 'A+'),('A-', 'A-'),('B+', 'B+'),('B-', 'B-'),('AB+', 'AB+'),('AB-', 'AB-'),('O+', 'O+'),('O-', 'O-')], string='Tipo de sangre')
    email = fields.Char(string='Correo electrónico', required=True)
    estado = fields.Selection(STATE_SELECTION, string='Estado', default='activo', required=True)
    sexo = fields.Selection(SEX_SELECTION, string='Sexo', required=True)
    jornada = fields.Selection(JOR_SELECTION, string='Jornada laboral', required=True)
    tipos_licencia_conducir = fields.Selection([
        ('a1', 'A1 - Motocicletas'),
        ('a2', 'A2 - Motocicletas'),
        ('a3', 'A3 - Motocicletas'),
        ('b1', 'B1 - Automóviles y camionetas'),
        ('b2', 'B2 - Automóviles y camionetas'),
        ('b3', 'B3 - Automóviles y camionetas'),
        ('c1', 'C1 - Camiones'),
        ('c2', 'C2 - Camiones'),
        ('c3', 'C3 - Camiones'),
    ], string='Tipos de Licencia de Conducir', multiple=True)
    
class control_mantenimiento_kilometraje(models.Model):
    _name = 'control.mantenimiento.kilometraje'
    _description = 'Registro de Kilometraje'


    kilometraje_actual = fields.Float(string='Kilometraje actual')
    proximo_mantenimiento = fields.Float(string='Próximo mantenimiento')
    mantenimiento_id = fields.Many2one('control.mantenimiento', string='Mantenimiento relacionado')
    kilometraje_faltante = fields.Float(string='Kilometraje faltante', compute='_compute_kilometraje_faltante')

    @api.depends('proximo_mantenimiento', 'kilometraje_actual')
    def _compute_kilometraje_faltante(self):
        for record in self:
            record.kilometraje_faltante = record.proximo_mantenimiento - record.kilometraje_actual
    
class control_mantenimiento(models.Model):
    _name = 'control.mantenimiento'
    _description = 'vehiculos'
    _rec_name = 'placa'

    combustible_selection = [
    ('gasolina', 'Gasolina'),
    ('diesel', 'Diésel'),
    ('gnc', 'Gas Natural Comprimido (GNC)'),
    ('glp', 'Gas Licuado del Petróleo (GLP)'),
    ('electricidad', 'Electricidad'),
    ('hidrogeno', 'Hidrógeno'),
    ('etanol', 'Etanol'),
    ('biodiesel', 'Biodiésel'),
    ]

    fecha = fields.Date(string='Fecha de Mantenimiento', required=True)
    tipo_mantenimiento = fields.Selection([
        ('preventivo', 'Preventivo'),
        ('correctivo', 'Correctivo'),
    ], string='Tipo de Mantenimiento', required=True)
    costo = fields.Float(string='Costo')
    descripcion = fields.Text(string='Descripción')
    vehiculo_marca = fields.Many2one('fabricante.vehiculo', string='Modelo', required=True, display_name='marca', domain="[('marca', '!=', False)]")
    vehiculo_imagen = fields.Binary(string='Imagen', compute='_compute_vehiculo_imagen', store=True)
    modelo_vehiculo = fields.Char(string='Modelo del Vehículo', required=True)
    responsable_id = fields.Many2one('ficha.empleados', string='Responsable de mantenimiento', required=True, domain="[('nombre', '!=', False)]")
    placa = fields.Char(string=' placa / VIN del Vehículo', required=True)
    ano = fields.Char(string='Año de fabricación', required=True)
    version = fields.Char(string='Versión del vehiculo', required=True)
    color = fields.Char(string='Color del vehiculo', required=True)
    combustible = fields.Selection(selection=combustible_selection,string='Tipo de Combustible',required=True)
    piezas_reemplazadas = fields.Char(string='Piezas Reemplazadas o Reparadas')
    proveedor_servicios = fields.Many2one('res.partner', string='Proveedor de Servicios', attrs={'invisible': [('tipo_mantenimiento', '!=', 'correctivo')]})
    adjuntos = fields.Many2many('ir.attachment', string='Adjuntar archivos')
    kilometrajes = fields.One2many('control.mantenimiento.kilometraje', 'mantenimiento_id', string='Kilometrajes')
    extintor = fields.Boolean(string='Contiene extintor')
    tipo_vehiculo = fields.Selection([
        ('auto', 'Automóvil'),
        ('camioneta', 'Camioneta'),
        ('moto', 'Motocicleta'),
    ], string='Tipo de Vehículo')

    @api.depends('vehiculo_marca')
    def _compute_vehiculo_imagen(self):
        for record in self:
            record.vehiculo_imagen = record.vehiculo_marca.imagen

    @api.onchange('tipo_mantenimiento')
    def _onchange_tipo_mantenimiento(self):
        if self.tipo_mantenimiento != 'correctivo':
            self.proveedor_servicios = False
    
    
class ficha_extintores(models.Model):
    _name = 'ficha.extintores'
    _description = 'extintores'

    placa_responsable = fields.Many2one('control.mantenimiento', string='Vehiculo asignado', required=True, display_name='placa', domain="[('placa', '!=', False)]")
    modelo_extintor = fields.Char(string='Modelo', required=True)
    fabricante_extintor = fields.Char(string='Fabricante del Extintor', required=True)
    capacidad = fields.Char(string='Capacidad', required=True)
    tiempo_descarga = fields.Char(string='Tiempo de Descarga Efectiva')
    alcance_efectivo = fields.Char(string='Alcance Efectivo')
    presion_trabajo = fields.Char(string='Presión de Trabajo')
    soporte_montaje = fields.Boolean(string='Soporte de Montaje')
    fecha_fabricacion = fields.Date(string='Fecha de Fabricación', required=True)
    fecha_vencimiento = fields.Date(string='Fecha de Vencimiento', compute='_compute_fecha_vencimiento', store=True)
    fecha_recarga = fields.Date(string='Fecha de Recarga')
    instrucciones_mantenimiento = fields.Text(string='Instrucciones de Mantenimiento')



        # Opciones para el manómetro de presión
    manometro_presion = fields.Selection([
        ('verde', 'Verde (Seguro)'),
        ('amarillo', 'Amarillo (Atención)'),
        ('rojo', 'Rojo (Recargar)'),
    ], string='Manómetro de Presión', required=True)

    # Campo para temperatura con rango de 0°C a 300°C
    temperatura_almacenamiento = fields.Float(string='Temperatura de Almacenamiento (°C)', min=0, max=300)

    # Opciones de clasificación de fuego
    clasificacion_fuego = fields.Selection([
        ('A', 'Clase A - Materiales Sólidos'),
        ('B', 'Clase B - Líquidos Inflamables'),
        ('C', 'Clase C - Gases Combustibles'),
        # Agrega más opciones según sea necesario
    ], string='Clasificación de Fuego', required=True)

    # Opciones de tipos de extintor
    tipo_extintor = fields.Selection([
        ('quimico_seco', 'Químico Seco'),
        ('agua', 'Agua'),
        ('co2', 'Dióxido de Carbono (CO2)'),
    ], string='Tipo de Extintor', required=True)

    @api.depends('fecha_fabricacion')
    def _compute_fecha_vencimiento(self):
        for extintor in self:
            if extintor.fecha_fabricacion:
                # Calcular la fecha de vencimiento en base a la vida útil del extintor
                # Puedes implementar aquí la lógica específica para calcular la fecha de vencimiento
                # por ejemplo, sumando un número de años a la fecha de fabricación.
                extintor.fecha_vencimiento = extintor.fecha_fabricacion + timedelta(days=365 * 5)  # Ejemplo de 5 años de vida útil


class SeguroVehiculo(models.Model):
    _name = 'seguro.vehiculo'
    _description = 'Gestión de Seguros de Vehículos'

    # Información de la Compañía de Seguros
    compania_seguros = fields.Char(string='Compañía de Seguros')
    numero_poliza = fields.Char(string='Número de Póliza')
    contacto_compania = fields.Char(string='Contacto de la Compañía')

    # Información del Vehículo Asegurado, los campos estan en el mantenimiento del vehiculo, con la placa se deben asignar automaticamente
    placa_responsable = fields.Many2one('control.mantenimiento', string='Placa / VIN del Vehículo', required=True, display_name='placa', domain="[('placa', '!=', False)]")
    vehiculo_marca = fields.Many2one('fabricante.vehiculo', string='Marca del Vehiculo', required=True, display_name='marca', domain="[('marca', '!=', False)]")
    modelo_vehiculo = fields.Char(string='Modelo del Vehículo')
    ano_vehiculo = fields.Char(string='Año del Vehículo')

    @api.onchange('placa_responsable')
    def _onchange_placa_responsable(self):
        if self.placa_responsable:
            mantenimiento = self.placa_responsable
            self.vehiculo_marca = mantenimiento.vehiculo_marca.id
            self.modelo_vehiculo = mantenimiento.modelo_vehiculo
            self.ano_vehiculo = mantenimiento.ano

    # Detalles de la Póliza
    tipo_cobertura = fields.Selection([
        ('responsabilidad', 'Responsabilidad'),
        ('completo', 'Completo'),
        # Agrega más tipos de cobertura si es necesario
    ], string='Tipo de Cobertura')
    fecha_inicio_poliza = fields.Date(string='Fecha de Inicio de la Póliza')
    fecha_fin_poliza = fields.Date(string='Fecha de Vencimiento de la Póliza')
    limite_cobertura = fields.Float(string='Límite de Cobertura')
    deducible = fields.Float(string='Deducible')

    # Detalles del Conductor Principal, estos datos tambien se asignan automaticamente con el manteniemnto 
    empleado_id = fields.Many2one('ficha.empleados', string='Empleado')   
    nombre_conductor = fields.Char(string='Nombre del Conductor')
    contacto_conductor = fields.Char(string='Contacto del Conductor')
    fecha_nacimiento_conductor = fields.Date(string='Fecha de Nacimiento del Conductor')
    licencia_conducir = fields.Char(string='Licencia de Conducir')

    @api.onchange('empleado_id')
    def _onchange_empleado_id(self):
        if self.empleado_id:
            empleado = self.empleado_id
            self.nombre_conductor = empleado.nombre
            self.contacto_conductor = empleado.celular
            self.fecha_nacimiento_conductor = empleado.fecha_nacimiento
            self.licencia_conducir = empleado.tipos_licencia_conducir

    # Historial de Accidentes
    accidente_ids = fields.One2many('seguro.accidente', 'seguro_id', string='Accidentes')

    # Reclamaciones
    reclamo_ids = fields.One2many('seguro.reclamo', 'seguro_id', string='Reclamaciones')

    # Documentos Relacionados
    documentos_poliza = fields.Many2many('ir.attachment', string='Documentos de la Póliza', relation='seguro_vehiculo_poliza_rel')
    documentos_reclamo = fields.Many2many('ir.attachment', string='Documentos de Reclamo', relation='seguro_vehiculo_reclamo_rel')


class SeguroAccidente(models.Model):
    _name = 'seguro.accidente'
    _description = 'Historial de Accidentes de Vehículos'

    seguro_id = fields.Many2one('seguro.vehiculo', string='Seguro')
    fecha_accidente = fields.Date(string='Fecha del Accidente')
    descripcion_accidente = fields.Text(string='Descripción del Accidente')
    detalles_danio = fields.Text(string='Detalles del Daño')
    informacion_terceros = fields.Text(string='Información de Terceros')
    fotos_accidente = fields.Many2many('ir.attachment', string='Fotos del Accidente')


class ReclamoSeguro(models.Model):
    _name = 'seguro.reclamo'
    _description = 'Reclamos de Seguro'

    seguro_id = fields.Many2one('seguro.vehiculo', string='Seguro')
    numero_reclamo = fields.Char(string='Número de Reclamo')
    fecha_reclamo = fields.Date(string='Fecha de Reclamo')
    estado_reclamo = fields.Selection([
        ('en_proceso', 'En Proceso'),
        ('resuelto', 'Resuelto'),
        ('rechazado', 'Rechazado'),
    ], string='Estado del Reclamo')
    monto_reclamo = fields.Float(string='Monto del Reclamo')
    documentos_reclamo = fields.Many2many('ir.attachment', string='Documentos del Reclamo')



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

