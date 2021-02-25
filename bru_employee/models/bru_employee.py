# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'hr.employee'

    identification_id = fields.Char(
        string=u'เลขประจำตัว'
    )
    affiliation_id = fields.Char(
        string=u'รหัสหน่วยงานสังกัด'
    )
    affiliation = fields.Char(
        string=u'หน่วยงานสังกัด'
    )
    operating_agency_id = fields.Char(
        string=u'รหัสหน่วยงานปฏิบัติ'
    )
    operating_agency = fields.Char(
        string=u'หน่วยงานปฏิบัติ'
    )

    # @api.constrains('department_id', 'user_id')
    # def _update_department_id(self):
    #     for rec in self:
    #         self.env['purchase.order'].sudo().search([
    #             ('name_id', '=', rec.user_id.id)
    #         ]).sudo().write({
    #             'department_id': rec.department_id.id
    #         })
