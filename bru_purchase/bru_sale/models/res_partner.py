# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ResPartner(models.Model):
    _inherit = 'res.partner'


    alley = fields.Char(
        string='Alley'
    )
    moo = fields.Char(
        string="Moo"
    )

    tambon_id = fields.Many2one(
        'tambon',
        string='Tambon',
    )
    amphur_id = fields.Many2one(
        'amphur',
        string='Amphur',
    )
    province_id = fields.Many2one(
        'province',
        string='Province',

    )
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


    @api.onchange('province_id')
    def _onchange_province_id(self):
        res = {}
        if self.province_id:
            if self.amphur_id.province_code != self.province_id.code:
                self.amphur_id = False
                self.tambon_id = False
            res['domain'] = {
                'amphur_id': [('province_code', '=', self.province_id.code)]
            }
            return res

    @api.onchange('amphur_id')
    def _onchange_amphur_id(self):
        condition = []
        if self.amphur_id:
            if self.tambon_id.amphur_code != self.amphur_id.code:
                self.tambon_id = False
            condition = [('amphur_code', '=', self.amphur_id.code)]
        return {'domain': {'tambon_id': condition}}

    @api.onchange('tambon_id')
    def _onchange_tambon_id(self):
        if self.tambon_id:
            zip = self.env['zip'].search(
                [('tambon_code', '=', self.tambon_id.code)]
            )
            self.zip = zip.name
