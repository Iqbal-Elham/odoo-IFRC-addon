# -*- coding: utf-8 -*-
# from odoo import http


# class Ifrc(http.Controller):
#     @http.route('/ifrc/ifrc', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ifrc/ifrc/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ifrc.listing', {
#             'root': '/ifrc/ifrc',
#             'objects': http.request.env['ifrc.ifrc'].search([]),
#         })

#     @http.route('/ifrc/ifrc/objects/<model("ifrc.ifrc"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ifrc.object', {
#             'object': obj
#         })
