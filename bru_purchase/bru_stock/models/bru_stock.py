# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

from datetime import datetime, timedelta, date


class BruStock(models.Model):
    _inherit = 'stock.picking'

    purchase_number = fields.Char(
        string='Purchase Request',
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
        'res.partner',
        related='purchase_id.name_id',
        string=u'เจ้าหน้าที่พัสดุ'
    )
    branch_id = fields.Many2one(
        'bru.faculty',
        # related='purchase_id.branch_id',
        string=u'สาขา'
    )
    faculty_ids = fields.Many2one(
        'bru.faculty',
        # related='purchase_id.faculty_ids',
        string=u'คณะ / สำนักงาน / ศูนย์'
    )
    bru_officer_id = fields.Many2one(
        'bru.branch',
        # related='purchase_id.bru_officer_id',
        string=u'ชื่อหน่วยงาน'
    )
    for_use = fields.Char(
        related='purchase_id.for_use',
        string=u'เพื่อใช้ในงานราชการ'
    )
    budget_id = fields.Many2one(
        'bru.budget',
        # related='purchase_id.budget_id',
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
        'res.partner',
        'name',
        related='purchase_id.people_purchase',
        string=u'คณะกรรมการจัดซื้อ / จัดจ้าง'
    )
    people_check_id = fields.One2many(
        'res.partner',
        'name',
        related='purchase_id.people_check_id',
        string=u'คณะกรรมการตรวจรับพัสดุ / การจ้าง'
    )
