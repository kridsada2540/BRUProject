# -*- coding: utf-8 -*-
from odoo import models, fields


class BruBudget(models.Model):
    _name = 'bru.budget'
    _rec_name = 'budget'
    _description = 'Bru Budget'

    budget_project = fields.Integer(
        required=True,
        string=u'จำนานเงินงบประมาณ'
    )
    year_budget_id = fields.Selection(
        selection=[
            ('2564', '2564'),
            ('2565', '2565'),
            ('2566', '2566'),
            ('2567', '2567'),
            ('2568', '2568'),
            ('2569', '2569'),
            ('2570', '2570')
        ],
        required=True,
        string=u'ปีงบประมาณ'
    )
    budget_id = fields.Selection(
        selection=[
            ('01', '01'),
            ('02', '02')
        ],
        string=u'รหัสงบประมาณ'
    )
    department_id = fields.Many2one(
        'hr.department',
        store=True,
        required=True,
        string=u'คณะ / สำนักงาน / ศูนย์',

    )
    budget = fields.Char(
        required=True,
        string=u'ชื่องบประมาณ'
    )
    product_id = fields.Char(
        size=10,
        string=u'รหัสโครงการ / ผลผลิต'
    )
    product = fields.Char(
        required=True,
        string=u'โครงการ / ผลผลิต'
    )
    expense_cate_id = fields.Char(
        size=4,
        string=u'รหัสโหมดรายจ่าย'
    )
    expense_cate = fields.Char(
        required=True,
        string=u'หมวดรายจ่าย'
    )
    expenses_id = fields.Char(
        size=5,
        string=u'รหัสรายจ่าย'
    )
    expenses = fields.Char(
        required=True,
        string=u'รายจ่าย'
    )
    activity_id = fields.Char(
        string=u'รหัสกิจกรรม'
    )
    activity = fields.Char(
        required=True,
        string=u'กิจกรรม'
    )
    remain_budg_id = fields.Integer(
        readonly=True,
        string=u'งบประมาณคงเหลือ'
    )

