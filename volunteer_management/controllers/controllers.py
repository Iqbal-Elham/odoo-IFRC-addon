# -*- coding: utf-8 -*-
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request
from odoo import http, _


class VolunteerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super(VolunteerPortal, self)._prepare_home_portal_values(counters)
        # rtn['volunteer_counts'] = request.env['vms.volunteer'].search_count([])
        return rtn


    @http.route(['/my', '/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):
        values = self._prepare_portal_layout_values()
        return request.render("volunteer_management.home_id", values)

    @http.route(['/my/profile'], auth="user", type='http', website=True)
    def weblearnsvolunteerFormView(self, **kw):
        volunteer_id = request.env['vms.volunteer'].search([('related_user', '=', request.uid)])
        vals = {"volunteer": volunteer_id, 'page_name':'volunteers_form_view'}
        # volunteer_records = request.env['vms.volunteer'].search([])
        # volunteer_ids = volunteer_records.ids
        # volunteer_index = volunteer_ids.index(volunteer_id.id)
        # if volunteer_index != 0 and volunteer_ids[volunteer_index - 1]:
            # vals['prev_record'] = '/my/volunteer/{}'.format(volunteer_ids[volunteer_index-1])
        # if volunteer_index < len(volunteer_ids) - 1 and volunteer_ids[volunteer_index+1]:
            # vals['next_record'] = '/my/volunteer/{}'.format(volunteer_ids[volunteer_index+1])
        return request.render("volunteer_management.wb_volunteers_form_view_portal", vals)
