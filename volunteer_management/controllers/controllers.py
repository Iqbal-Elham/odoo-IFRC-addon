# -*- coding: utf-8 -*-
# from odoo import http


# class VolunteerManagement(http.Controller):
#     @http.route('/volunteer_management/volunteer_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/volunteer_management/volunteer_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('volunteer_management.listing', {
#             'root': '/volunteer_management/volunteer_management',
#             'objects': http.request.env['volunteer_management.volunteer_management'].search([]),
#         })

#     @http.route('/volunteer_management/volunteer_management/objects/<model("volunteer_management.volunteer_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('volunteer_management.object', {
#             'object': obj
#         })
