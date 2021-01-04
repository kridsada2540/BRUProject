# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Faculty(models.Model):
    _name = 'bru.faculty'
    _description = 'BRU Faculty'

    name = fields.Char(
        string=u'คณะ'
    )
    branch_id = fields.One2many(
        'faculty.branch',
        'faculty_id',
        string=u'สาขา'
    )