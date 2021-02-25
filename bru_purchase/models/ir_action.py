from odoo import api, models


class IR(models.Model):
    _inherit = 'ir.actions.act_window'

    @api.multi
    def read(self, fields=None, load='_classic_read'):
        res = super(IR, self).read(fields, load)

        if not res:
            return res

        if res[0].get('domain'):
            if "('id', '=', 1)" in res[0]['domain']:
                    domain = str(('id', 'in', self._get_ids()))
                    res[0]['domain'] = res[0]['domain'].replace(
                        "('id', '=', 1)", domain
                    )
        return res

    def _get_ids(self):
        ids = []
        if self.user_has_groups('purchase.group_purchase_user'):
            ids = self.env['purchase.order'].sudo().search([
                ('create_uid', '=', self.env.user.id),
            ]).ids
            ids.append(0)
            print ids
        if self.user_has_groups('purchase.group_purchase_manager'):
            ids = self.env['purchase.order'].search([
                ('name_id.department_id', '=', self.env["hr.employee"].sudo().search([('user_id', '=', self.env.user.id)]).department_id.id),
            ]).ids

            for line in self.env['purchase.order'].search([
                ('name_id.department_id.parent_id', '=', self.env["hr.employee"].sudo().search([('user_id', '=', self.env.user.id)]).department_id.id)
            ]).ids:
                ids.append(line)

        if self.user_has_groups('bru_employee.group_employee_chancellor'):
            ids = self.env['purchase.order'].sudo().search([
                ('amount_total', '>=', 50000),
            ]).ids
        if self.user_has_groups('bru_employee.group_employee_dean'):
            ids = self.env['purchase.order'].search([
                ('amount_total', '<', 50000),
                ('name_id.department_id', '=', self.env["hr.employee"].sudo().search([('user_id', '=', self.env.user.id)]).department_id.id),
            ]).ids
        return ids


