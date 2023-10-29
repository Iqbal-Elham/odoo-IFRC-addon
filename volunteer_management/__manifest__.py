# -*- coding: utf-8 -*-
{
    "name": "Volunteer Management System",
    "summary": """
        Volunteer Management System
        """,
    "description": """
        Long description of module's purpose
    """,
    "author": "My Company",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    "sequence": "-1000",
    "application": True,
    # any module necessary for this one to work correctly
    "depends": ["base", "portal"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/volunteers.xml",
        "views/volunteers_certificates.xml",
        "views/volunteers_deployments.xml",
        "views/volunteers_trainings.xml",
        "views/portal_views.xml",
    ],
}
