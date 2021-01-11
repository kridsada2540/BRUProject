# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'hr.employee'

    language = fields.Selection(
        selection=[
            ('en_US', u'English'),
            ('th_TH', u'Thai'),
        ],
        string=u'Language'
    )
    identification_id = fields.Integer(
        string=u'เลขประจำตัว'
    )
    affiliation_id = fields.Integer(
        string=u'รหัสหน่วยงานสังกัด'
    )
    affiliation = fields.Char(
        string=u'หน่วยงานสังกัด'
    )
    operating_agency_id = fields.Integer(
        string=u'รหัสหน่วยงานปฏิบัติ'
    )
    operating_agency = fields.Char(
        string=u'หน่วยงานปฏิบัติ'
    )

