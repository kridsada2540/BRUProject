# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    department_id = fields.Many2one(
        'hr.department',
        store=True,
        string=u'คณะ / สำนักงาน / ศูนย์',
    )



