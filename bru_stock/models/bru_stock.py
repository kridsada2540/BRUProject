# -*- coding: utf-8 -*-
from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)


class BruStock(models.Model):
    _inherit = 'stock.picking'

    prod_id = fields.Many2one(
        'purchase.order',
        required=True,
        string='Product'
    )

    purchase_number = fields.Char(
        string='Purchase Request',
        related='purchase_id.purchase_number',
        readonly=True
    )
    document_type = fields.Selection(
        selection=[
            ('PR01', u'PR01=ขออนุมัติซื้อวัสดุ'),
            ('PR02', u'PR02=ขออนุมัติซื้อครุภัณฑ์'),
            ('PR03', u'PR03=ขออนุมัติจัดจ้าง')
        ],
        related='purchase_id.document_type',
        string=u'ประเภทเอกสาร'
    )
    years = fields.Selection(
        selection=[
            ('2560', '2560'),
            ('2561', '2561'),
            ('2562', '2562'),
            ('2563', '2563'),
            ('2564', '2564'),
            ('2565', '2565'),
            ('2566', '2566'),
            ('2567', '2567'),
            ('2568', '2568'),
            ('2569', '2569'),
            ('2570', '2570')
        ],
        related='purchase_id.years',
        string=u'ปีงบประมาณ'
    )
    name_id = fields.Many2one(
        'hr.employee',
        related='purchase_id.name_id',
        string=u'เจ้าหน้าที่พัสดุ'
    )
    # branch_id = fields.Many2one(
    #     'faculty.branch',
    #     related='purchase_id.branch_id',
    #     string=u'สาขา'
    # )
    department_id = fields.Many2one(
        'hr.department',
        related='purchase_id.department_id',
        string=u'คณะ / สำนักงาน / ศูนย์'
    )
    bru_officer_id = fields.Many2one(
        'bru.branch',
        related='purchase_id.bru_officer_id',
        string=u'ชื่อหน่วยงาน'
    )
    for_use = fields.Char(
        related='purchase_id.for_use',
        string=u'เพื่อใช้ในงานราชการ'
    )
    budget_id = fields.Many2one(
        'bru.budget',
        related='purchase_id.budget_id',
        string=u'ชื่องบประมาณ'
    )
    product = fields.Char(
        related='purchase_id.product',
        readonly=True,
        string=u'ผลผลิต'
    )
    expenses = fields.Char(
        related='purchase_id.expenses',
        readonly=True,
        string=u'รายจ่าย'
    )
    activity = fields.Char(
        related='purchase_id.activity',
        readonly=True,
        string=u'กิจกรรม'
    )
    detail = fields.Char(
        related='purchase_id.detail',
        string=u'รายละเอียด'
    )
    remain_budg_id = fields.Integer(
        readonly=True,
        related='purchase_id.remain_budg_id',
        string=u'ยอดงบประมาณคงเหลือ'
    )
    people_purchase = fields.One2many(
        'picking.hr.employee.purchase',
        'picking_id',
        string=u'คณะกรรมการจัดซื้อ / จัดจ้าง',
    )
    people_check_id = fields.One2many(
        'picking.hr.employee.check',
        'picking_id',
        string=u'คณะกรรมการตรวจรับพัสดุ / การจ้าง'
    )


    @api.multi
    def _create_backorder(self, backorder_moves=[]):
        for rec in self:
            backorders = super(BruStock, rec)._create_backorder(
                backorder_moves=backorder_moves)
            for back_order in backorders:
                if back_order.backorder_id:
                    # people purhcase
                    for purchase in back_order.backorder_id.people_purchase:
                        self.env['picking.hr.employee.purchase'].create({
                            'picking_id': back_order.id,
                            'employee_id': purchase.employee_id.id
                        })
                    # people check
                    for check in back_order.backorder_id.people_check_id:
                        self.env['picking.hr.employee.check'].create({
                            'picking_id': back_order.id,
                            'employee_id': check.employee_id.id,
                        })
            return backorders


class PickingResPartnerPurchase(models.Model):
    _name = 'picking.hr.employee.purchase'
    _description = 'Picking Employee Purchase'

    picking_id = fields.Many2one(
        comodel_name='stock.picking',
        string='Picking ID',
    )
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Name',
        required=True,
    )
    work_phone = fields.Char(
        # related='purchase_id.work_phone',
        size=10,
        readonly=True,
        string='Phone',
    )
    work_email = fields.Char(
        # related='purchase_id.work_email',
        readonly=True,
        string='E-mail',
    )


class PickingResPartnerCheck(models.Model):
    _name = 'picking.hr.employee.check'
    _description = 'Picking Employee Check'

    picking_id = fields.Many2one(
        comodel_name='stock.picking',
        string='Picking ID',
    )
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='Name',
        required=True,
    )
    work_phone = fields.Char(
        # related='purchase_id.work_phone',
        size=10,
        readonly=True,
        string='Phone',
    )
    work_email = fields.Char(
        # related='purchase_id.work_email',
        readonly=True,
        string='E-mail',
    )