# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class BRUSequencePurchase(models.Model):
    _name = 'sequence.purchase'


    name = fields.Char(
        string='Sequence'
    )
    model_id = fields.Many2one(
        'ir.model'
    )
    sequence_id = fields.Many2one(
        'ir.sequence',
        ondelete='restrict'
    )