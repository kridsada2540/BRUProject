# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class BruPurchase(models.Model):
    _inherit = 'purchase.order'

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
        store=True,
        required=True,
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
        store=True,
        related='budget_id.year_budget_id',
        string=u'ปีงบประมาณ'
    )
    name_id = fields.Many2one(
        'res.partner',
        store=True,
        string=u'เจ้าหน้าที่พัสดุ',
        default=lambda self: self.env.user.partner_id,
    )
    branch_id = fields.Many2one(
        'faculty.branch',
        store=True,
        string=u'สาขา',
        # related='res_partner.branch_id',
        default=lambda self: self.env.user.partner_id.faculty_branch,
    )
    faculty_ids = fields.Many2one(
        'bru.faculty',
        store=True,
        string=u'คณะ / สำนักงาน / ศูนย์',
        # related='res_partner.faculty_ids',
        default=lambda self: self.env.user.partner_id.faculty_ids,
    )
    bru_officer_id = fields.Many2one(
        'bru.branch',
        store=True,
        string=u'ชื่อหน่วยงาน'
    )
    for_use = fields.Char(
        store=True,
        string=u'เพื่อใช้ในงานราชการ'
    )
    budget_id = fields.Many2one(
        'bru.budget',
        store=True,
        string=u'ชื่องบประมาณ'
    )
    product = fields.Char(
        store=True,
        related='budget_id.product',
        readonly=True,
        string=u'ผลผลิต'
    )
    expenses = fields.Char(
        related='budget_id.expenses',
        readonly=True,
        store=True,
        string=u'รายจ่าย'
    )
    activity = fields.Char(
        related='budget_id.activity',
        readonly=True,
        store=True,
        string=u'กิจกรรม'
    )
    detail = fields.Char(
        store=True,
        string=u'รายละเอียด'
    )
    remain_budg_id = fields.Integer(
        readonly=True,
        store=True,
        related='budget_id.remain_budg_id',
        string=u'ยอดงบประมาณคงเหลือ'
    )
    people_purchase = fields.One2many(
        'res.partner.purchase',
        'purchase_id',
        store=True,
        string=u'คณะกรรมการจัดซื้อ / จัดจ้าง'
    )
    people_check_id = fields.One2many(
        'res.partner.check',
        'purchase_id',
        store=True,
        string=u'คณะกรรมการตรวจรับพัสดุ / การจ้าง'
    )

    @api.multi
    def button_confirm(self):
        res = super(BruPurchase, self).button_confirm()
        for order in self:
            remain = order.budget_id.remain_budg_id
            if remain == 0:
                cash_balance = order.budget_id.name - order.amount_total
                if cash_balance < 0:
                    raise UserError(_(u'ยอดเกินกำหนดการสั่งซื้อ!!!'))
                order.budget_id.remain_budg_id = cash_balance
            elif remain > 0:
                cash_balance2 = remain - order.amount_total
                if cash_balance2 < 0:
                    raise UserError(_(u'ยอดเกินกำหนดการสั่งซื้อ!!!'))
                order.budget_id.remain_budg_id = cash_balance2
        return res

    @api.model
    def create(self, values):
        request_purchase = super(BruPurchase, self).create(values)
        request_purchase.purchase_number = request_purchase.document_type + \
            request_purchase.create_sequence()
        return request_purchase

    def create_sequence(self):
        sequence_template = self.env.ref(
            'bru_purchase.sequence_purchase_request_id')
        model = self.env['ir.model'].sudo().search([
            ('name', '=', 'Purchase Order')
        ], limit=1)

        seq = self.env['sequence.purchase'].sudo().search([
            ('name', '=', 'Sequence Purchase Request'),
            ('model_id', '=', model.id),
        ], order='id desc', limit=1)

        if not seq:
            seq_temp = sequence_template.sudo().copy()
            seq_temp.write({
                'code': 'Sequence Purchase Request',
                'name': 'Sequence Purchase Request',
                # 'prefix': 'CN',
            })
            seq = self.env['sequence.purchase'].sudo().create({
                'name': 'Sequence Purchase Request',
                'model_id': model.id,
                'sequence_id': seq_temp.id,
            })
        return seq.sequence_id.next_by_id()


class ResPartnerPurchase(models.Model):
    _name = 'res.partner.purchase'
    _description = 'Partner Purchase'

    purchase_id = fields.Many2one(
        comodel_name='purchase.order',
        string='Purchase ID',
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Name',
        required=True,
    )
    phone = fields.Char(
        related='partner_id.phone',
        string='Phone',
    )
    email = fields.Char(
        related='partner_id.email',
        string='E-mail',
    )
    is_purchase = fields.Boolean(
        string='Is Partner Purchase',
        default=True,
    )


class ResPartnerCheck(models.Model):
    _name = 'res.partner.check'
    _description = 'Partner Check'

    purchase_id = fields.Many2one(
        comodel_name='purchase.order',
        string='Purchase ID',
    )
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Name',
        required=True,
    )
    phone = fields.Char(
        related='partner_id.phone',
        string='Phone',
    )
    email = fields.Char(
        related='partner_id.email',
        string='E-mail',
    )
    is_purchase = fields.Boolean(
        string='Is Partner Purchase',
        default=False,
    )
