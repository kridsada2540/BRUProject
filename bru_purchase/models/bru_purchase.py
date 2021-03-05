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
        'hr.employee',
        string=u'เจ้าหน้าที่พัสดุ',
        default=lambda self: self._get_name_id(),
    )
    department_id = fields.Many2one(
        'hr.department',
        string=u'คณะ / สาขา',
        related='name_id.department_id',
    )
    # faculty_id = fields.Many2one(
    #     'hr.department',
    #     store=True,
    #     string=u'คณะ / สาขา',
    #     # default=lambda self: self.env.user.employee_id.department_id,
    #     # related='hr_employee.employee_id.department_id',
    #     # default=lambda self: self.env.user.res.users.department_id,
    # )
    bru_officer_id = fields.Many2one(
        'bru.branch',
        string=u'ชื่อหน่วยงาน',
        required = True,
    )
    for_use = fields.Char(
        store=True,
        string=u'เพื่อใช้ในงานราชการ'
    )
    budget_id = fields.Many2one(
        'bru.budget',
        store=True,
        string=u'ชื่องบประมาณ',
        required=True
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
        related='budget_id.remain_budg_id',
        string=u'ยอดงบประมาณคงเหลือ'
    )
    type_product = fields.Many2one(
        'bru.type',
        string='Type'
    )
    people_purchase = fields.One2many(
        'hr.employee.purchase',
        'purchase_id',
        store=True,
        required=True,
        string=u'คณะกรรมการจัดซื้อ / จัดจ้าง'
    )
    people_check_id = fields.One2many(
        'hr.employee.check',
        'purchase_id',
        store=True,
        required=True,
        string=u'คณะกรรมการตรวจรับพัสดุ / การจ้าง'
    )
    can_confirm = fields.Boolean(
        string="Can Confirm ?",
        compute="_compute_can_confirm",
    )

    # @api.depends('create')
    # def _compute_department_id(self):
    #     for rec in self:
    #         rec.department_id = self.env["hr.employee"].sudo().search([('user_id', '=', rec.name_id.id)]).department_id.id

    @api.model
    def _get_name_id(self):
        employee = self.env["hr.employee"].search([('user_id', '=', self.env.user.id)])
        return len(employee) == 1 and employee or False

    @api.multi
    def _compute_can_confirm(self):
        for rec in self:
            can_confirm = False
            if rec.amount_total > 50000 and self.env.user.has_group('bru_purchase.group_purchase_chancellor'):
                can_confirm = True
            if rec.amount_total <= 50000 and self.env.user.has_group('bru_purchase.group_purchase_dean'):
                can_confirm = True
            rec.can_confirm = can_confirm
        return rec

    @api.multi
    def button_cancel(self):
        res = super(BruPurchase, self).button_cancel()
        for order in self:
            can_confirm = False
            if order.amount_total > 50000 and self.env.user.has_group('bru_purchase.group_purchase_chancellor'):
                can_confirm = True
            if order.amount_total <= 50000 and self.env.user.has_group('bru_purchase.group_purchase_dean'):
                can_confirm = True
            order.can_confirm = can_confirm
        return res

    @api.multi
    def button_confirm(self):
        res = super(BruPurchase, self).button_confirm()
        for order in self:
            remain = order.budget_id.remain_budg_id
            if remain == 0:
                cash_balance = order.budget_id.budget_project - order.amount_total
                if cash_balance < 0:
                    raise UserError(_(u'ยอดเกินกำหนดการสั่งซื้อ!!!'))
                order.budget_id.remain_budg_id = cash_balance
                print (cash_balance)
            elif remain > 0:
                cash_balance2 = remain - order.amount_total
                if cash_balance2 < 0:
                    raise UserError(_(u'ยอดเกินกำหนดการสั่งซื้อ!!!'))
                order.budget_id.remain_budg_id = cash_balance2
                print (cash_balance2)
        return res

    # @api.multi
    # def button_cancel(self):
    #     res = super(BruPurchase, self).button_cancel()
    #     for order in self:
    #         order.budget_id.remain_budg_id += order.amount_total
    #     return res

    @api.model
    def create(self, values):
        request_purchase = super(BruPurchase, self).create(values)
        request_purchase.purchase_number = request_purchase.document_type + request_purchase.create_sequence()
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
    _name = 'hr.employee.purchase'
    _description = 'Employee Purchase'

    purchase_id = fields.Many2one(
        comodel_name='purchase.order',
        string='Purchase ID',
    )
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='ชื่อคณะกรรมการ',
        required=True,
    )
    job_id = fields.Many2one(
        related='employee_id.job_id',
        readonly=True,
        string=u'ตำแหน่งงาน',
    )
    is_purchase = fields.Boolean(
        string='Is Partner Purchase',
        default=True,
    )


class ResPartnerCheck(models.Model):
    _name = 'hr.employee.check'
    _description = 'Employee Check'

    purchase_id = fields.Many2one(
        comodel_name='purchase.order',
        string='Purchase ID',
    )
    employee_id = fields.Many2one(
        comodel_name='hr.employee',
        string='ชื่อคณะกรรมการ',
        required=True,
    )
    job_id = fields.Many2one(
        related='employee_id.job_id',
        readonly=True,
        string=u'ตำแหน่งงาน',
    )
    is_purchase = fields.Boolean(
        string='Is Partner Purchase',
        default=True,
    )

class EmployeeDepartment(models.Model):
    _inherit = 'hr.employee'
