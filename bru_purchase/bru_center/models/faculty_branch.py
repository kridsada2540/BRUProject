# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FacultyBranch(models.Model):
    _name = 'faculty.branch'
    _description = 'BRU Faculty Branch'

    name = fields.Char(
        string=u'สาขา'
    )
    faculty_id = fields.Many2one(
        'bru.faculty',
        string=u'คณะ'
    )