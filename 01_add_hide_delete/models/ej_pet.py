# -*- coding: utf-8 -*-

from odoo import api, fields, models

class EjPet(models.Model):
    _inherit = 'ej.pet'
    piel = fields.Char(string='Piel', default='Verde')
    paseo = fields.Boolean(string='Paseo')

    is_racism = fields.Boolean(string='Is racism', compute='_compute_is_racism')

    date_b = fields.Date('Fecha', default=fields.Date.today)

    @api.depends('piel')
    def _compute_is_racism(self):
        for record in self:
            record.is_racism = record.piel == 'Negro'