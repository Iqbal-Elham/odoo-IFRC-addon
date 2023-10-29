# -*- coding: utf-8 -*-
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request


class VolunteerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super()._prepare_home_portal_values(counters)
        # rtn['volunteer_count'] = request.env['vms.volunteer'].search_count([])
        return rtn
