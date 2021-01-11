# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    language = fields.Selection(
        selection=[
            ('en_US', u'English'),
            ('th_TH', u'Thai'),
        ],
        string=u'Language'
    )


