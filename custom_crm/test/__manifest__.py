# -*- coding: utf-8 -*-
{
    'name': "test",

    'summary': """ Control vehicular  """,

    'description': """
        Se realizara un inventario donde la base de datos solo tendran acceso los jefes, del resto 
        seran modulos para ampliar la informacion dentro de la base de datos con seleccion multiple
        Es un modelo de prueba para responder a las necesidades basicas de la empresa JMV en cuanto a 
        industria mortriz llevando a cabo un control sobre la flota vehicular.
    """,

    'author': "Valery Cuadros - Analista IT",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable' : True, 

    'application' : True,
}
