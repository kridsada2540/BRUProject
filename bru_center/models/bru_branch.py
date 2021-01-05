# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BruBrach(models.Model):
    _name = 'bru.branch'
    _rec_name = 'bru_officer_branch'
    _description = 'Bru Branch'

    bru_officer_branch_id = fields.Integer(
        string=u'รหัสหน่วยงาน'
    )
    bru_officer_branch = fields.Char(
        string=u'ชื่อหน่วยงาน'
    )
    organization_level_id = fields.Selection(
        selection=[
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4')

        ],
        string=u'ระดับหน่วยงาน'
    )
    organization_id = fields.Selection(
        selection=[
            ('1', u'มหาวิทยาลัย'),
            ('2', u'คณะ / สำนักงาน / เทียบเท่า'),
            ('3', u'สำนักงาน / กอง / กลุ่มงาน / เที่ยบเท่า'),
            ('4', u'งาน / ฝ่าย / เทียบเท่า')
        ],
        string=u'ชื่อ / ระดับหน่วยงาน'
    )

    @api.onchange('organization_level_id')
    def _onchang_organization_level(self):
        for rec in self:
            if rec.organization_level_id:
                rec.organization_id = rec.organization_level_id
