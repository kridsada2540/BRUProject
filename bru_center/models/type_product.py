# -*- coding: utf-8 -*-
from odoo import models, fields, api

class TypeProduct(models.Model):
    _name = 'bru.type'
    _rec_name = 'type_product'
    _description = 'Type Product'

    type_product = fields.Char(
        string=u'Type'
    )
