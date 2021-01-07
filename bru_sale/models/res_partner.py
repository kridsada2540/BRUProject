# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    faculty_ids = fields.Many2one(
        'bru.faculty',
        string=u'คณะ'
    )
    faculty_branch = fields.Many2one(
        'faculty.branch',
        string=u'สาขา'
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

