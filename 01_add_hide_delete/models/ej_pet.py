# -*- coding: utf-8 -*-

from odoo import api, fields, models

class EjPet(models.Model):
    _inherit = 'ej.pet'
    piel = fields.Char(string='Piel', default='Verde')
    paseo = fields.Boolean(string='Paseo')
