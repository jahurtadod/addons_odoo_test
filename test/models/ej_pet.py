from odoo import api, fields, models

class EjPet(models.Model):
    _name = 'ej.pet'
    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age', required=True)
    color = fields.Char(string='color', required=True)
    type = fields.Selection([('small', 'Small'),
                             ('medium', 'Medium'),
                             ('big', 'Big')], string='type', default="small", required=True)
