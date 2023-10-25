# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Volunteer(models.Model):
    _name = 'vms.volunteer'
    _description = 'Volunteers'

    name = fields.Char()
    father_name = fields.Char()
    tazkira_number = fields.Char()
    dob = fields.Date()
    age = fields.Integer()
    
    mobile = fields.Char()
    photo = fields.Image()
    specialization = fields.Char()

    gender = fields.Selection([('male', 'male'), ('female', 'female')])
    marital_status = fields.Selection([
        ("S", "Single"),
        ("M", "Married"),
        ("D", "Divorced"),
        ("W", "Widowed"),
        ("E", "Engaged"),
    ])
    blood_group = fields.Selection([
        ("A+", "A Positive"),
        ("A-", "A Negative"),
        ("B+", "B Positive"),
        ("B-", "B Negative"),
        ("AB+", "AB Positive"),
        ("AB-", "AB Negative"),
        ("O+", "O Positive"),
        ("O-", "O Negative"),
    ])
    # state = fields.Selection([])

    # occupation = fields.Many2one()
    # languages = fields.Many2many()
    # disabilities = fields.One2many()
    # type_of_volunteer = fields.Many2one()
    # permanent_province = fields.Many2one()
    # permanent_district = fields.Many2one()
    # current_province = fields.Many2one()
    # current_district = fields.Many2one()
    # emergency_contacts = fields.One2many()
    # education_degree = fields.Many2one()
    # documents = fields.One2many()
    # related_user = fields.Many2one()
    # deployments = fields.One2many()
    # certificates = fields.One2many()
    # trainings = fields.One2many()

    partner_id = fields.Many2one('res.partner')

    place_of_work = fields.Char()
    number_of_children = fields.Integer()
    driver_license = fields.Boolean()
    permanent_village = fields.Char()
    permanent_school_mosque = fields.Char()
    current_village = fields.Char()
    current_school_mosque = fields.Char()
    university_school = fields.Char()
    comments = fields.Text()