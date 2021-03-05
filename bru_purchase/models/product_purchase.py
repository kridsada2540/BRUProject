# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class BruPurchase(models.Model):
    _inherit = 'product.template'

    type_product = fields.Many2one(
        'bru.type',
        string='Type'
    )