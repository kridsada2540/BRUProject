# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BruBudget(models.Model):
    _name = 'bru.budget'
    _rec_name = 'budget'
    _description = 'Bru Budget'


    name = fields.Integer(
        string=u'จำนานเงินงบประมาณ'
    )
    year_budget_id = fields.Selection(
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
        string=u'ปีงบประมาณ'
    )
    budget_id = fields.Integer(
        string=u'รหัสงบประมาณ'
    )
    budget = fields.Char(
        string=u'ชื่องบประมาณ'
    )
    faculty_ids = fields.Many2one(
        'bru.faculty',
        string=u'คณะ / หน่วยงาน'
    )
    product_id = fields.Integer(
        string=u'รหัสโครงการ / ผลผลิต'
    )
    product = fields.Char(
        string=u'โครงการ / ผลผลิต'
    )
    expense_cate_id = fields.Integer(
        string=u'รหัสโหมดรายจ่าย'
    )
    expense_cate = fields.Char(
        string=u'หมวดรายจ่าย'
    )
    expenses_id = fields.Integer(
        string=u'รหัสรายจ่าย'
    )
    expenses = fields.Char(
        string=u'รายจ่าย'
    )
    activity_id = fields.Integer(
        string=u'รหัสกิจกรรม'
    )
    activity = fields.Char(
        string=u'กิจกรรม'
    )
    remain_budg_id = fields.Integer(
        readonly=True,
        string=u'งบประมาณคงเหลือ'
    )

