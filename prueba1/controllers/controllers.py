# -*- coding: utf-8 -*-
# from odoo import http


# class Prueba1(http.Controller):
#     @http.route('/prueba1/prueba1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prueba1/prueba1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prueba1.listing', {
#             'root': '/prueba1/prueba1',
#             'objects': http.request.env['prueba1.prueba1'].search([]),
#         })

#     @http.route('/prueba1/prueba1/objects/<model("prueba1.prueba1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prueba1.object', {
#             'object': obj
#         })
