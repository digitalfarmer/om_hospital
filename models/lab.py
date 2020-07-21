from odoo import  models, fields

class HospitalLab(models.Model):
    _name = 'hospital.lab'
    _description = 'Hospital Laboratory'

    name = fields.Char('Name', required=True)
    user_id= fields.Many2one('res.users', 'Responsible')