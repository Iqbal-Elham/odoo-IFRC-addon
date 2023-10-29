# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Volunteer(models.Model):
    _name = "vms.volunteer"
    _description = "Volunteers"

    name = fields.Char()
    father_name = fields.Char()
    tazkira_number = fields.Char()
    dob = fields.Date()
    age = fields.Integer()

    mobile = fields.Char()
    photo = fields.Image()

    gender = fields.Selection([("male", "male"), ("female", "female")])
    marital_status = fields.Selection(
        [
            ("S", "Single"),
            ("M", "Married"),
            ("D", "Divorced"),
            ("W", "Widowed"),
            ("E", "Engaged"),
        ]
    )
    blood_group = fields.Selection(
        [
            ("A+", "A Positive"),
            ("A-", "A Negative"),
            ("B+", "B Positive"),
            ("B-", "B Negative"),
            ("AB+", "AB Positive"),
            ("AB-", "AB Negative"),
            ("O+", "O Positive"),
            ("O-", "O Negative"),
        ]
    )

    related_user = fields.Many2one("res.users")

    state = fields.Selection([("approved", "Approved"), ("rejected", "Rejected")])

    permanent_province = fields.Many2one("vms.province", string="Permanent Province")
    permanent_district = fields.Many2one("vms.district", string="Permanent District")
    current_province = fields.Many2one("vms.province", string="Current Province")
    current_district = fields.Many2one("vms.district", string="Current District")
    type_of_volunteer = fields.Many2one(
        "vms.volunteer.type", string="Type of Volunteer"
    )
    occupation = fields.Many2one("vms.occupation", string="Occupation")
    specialization = fields.Char()
    education_degree = fields.Many2one(
        "vms.education.degree", string="Education Degree"
    )
    place_of_work = fields.Char()
    languages = fields.Many2many("vms.language", string="Languages")
    number_of_children = fields.Integer()
    driver_license = fields.Boolean()
    permanent_village = fields.Char()
    permanent_school_mosque = fields.Char()
    current_village = fields.Char()
    current_school_mosque = fields.Char()
    university_school = fields.Char()
    comments = fields.Text()
    disabilities = fields.One2many(
        "vms.disability", "volunteer_id", string="Disabilities"
    )
    emergency_contacts = fields.One2many(
        "vms.emergency.contact", "volunteer_id", string="Emergency Contacts"
    )
    documents = fields.One2many("vms.document", "volunteer_id", string="Documents")

    # not used ------------
    deployments = fields.One2many(
        "vms.deployment", "volunteer_id", string="Deployments"
    )
    certificates = fields.One2many(
        "vms.certificate", "volunteer_id", string="Certificates"
    )
    trainings = fields.One2many("vms.training", "volunteer_id", string="Trainings")

    def open_deployments(self):
        for rec in self:
            return {
                "name": "Deployments",
                "type": "ir.actions.act_window",
                "view_mode": "tree,form",
                "res_model": "vms.deployment",  # Replace with your actual model name
                "domain": [("volunteer_id", "=", rec.id)],
            }

    # Action function to open Certificates
    def open_certificates(self):
        for rec in self:
            return {
                "name": "Certificates",
                "type": "ir.actions.act_window",
                "view_mode": "tree,form",
                "res_model": "vms.certificate",  # Replace with your actual model name
                "domain": [("volunteer_id", "=", rec.id)],
            }

    # Action function to open Trainings
    def open_trainings(self):
        for rec in self:
            # Set the user's groups to the portal group
            # groups_id = self.env["res.groups"].browse(10)

            # self.env["res.users"].create(
            #     {
            #         "email": "portal@gmail.com",
            #         "login": "portal@gmail.com",
            #         "name": "ahmad",
            #         "groups_id": groups_id,
            #     }
            # )

            return {
                "name": "Trainings",
                "type": "ir.actions.act_window",
                "view_mode": "tree,form",
                "res_model": "vms.training",  # Replace with your actual model name
                "domain": [("volunteer_id", "=", rec.id)],
            }


class Occupation(models.Model):
    _name = "vms.occupation"
    _description = "Occupation"

    name = fields.Char(string="Occupation", required=True)


class Language(models.Model):
    _name = "vms.language"
    _description = "Language"

    name = fields.Char(string="Language", required=True)


class Disability(models.Model):
    _name = "vms.disability"
    _description = "Disability"

    name = fields.Char(string="Disability", required=True)
    volunteer_id = fields.Many2one("vms.volunteer", string="Volunteer")


class VolunteerType(models.Model):
    _name = "vms.volunteer.type"
    _description = "Type of Volunteer"

    name = fields.Char(string="Type of Volunteer", required=True)


class Province(models.Model):
    _name = "vms.province"
    _description = "Province"

    name = fields.Char(string="Province", required=True)


class District(models.Model):
    _name = "vms.district"
    _description = "District"

    name = fields.Char(string="District", required=True)


class EmergencyContact(models.Model):
    _name = "vms.emergency.contact"
    _description = "Emergency Contact"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone")
    volunteer_id = fields.Many2one("vms.volunteer", string="Volunteer")


class EducationDegree(models.Model):
    _name = "vms.education.degree"
    _description = "Education Degree"

    name = fields.Char(string="Education Degree", required=True)


class Document(models.Model):
    _name = "vms.document"
    _description = "Document"

    name = fields.Char(string="Name", required=True)
    volunteer_id = fields.Many2one("vms.volunteer", string="Volunteer")
    document_file = fields.Binary(string="Document")


class Deployment(models.Model):
    _name = "vms.deployment"
    _description = "Deployment"

    name = fields.Char(string="Deployment", required=True)
    volunteer_id = fields.Many2one("vms.volunteer", string="Volunteer")


class Certificate(models.Model):
    _name = "vms.certificate"
    _description = "Certificate"

    name = fields.Char(string="Certificate", required=True)
    volunteer_id = fields.Many2one("vms.volunteer", string="Volunteer")


class Training(models.Model):
    _name = "vms.training"
    _description = "Training"

    name = fields.Char(string="Training", required=True)
    volunteer_id = fields.Many2one("vms.volunteer", string="Volunteer")
