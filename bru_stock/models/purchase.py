# -*- coding: utf-8 -*-
from odoo import models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.multi
    def button_approve(self, force=False):
        res = super(PurchaseOrder, self).button_approve(force=force)
        for rec in self:
            for picking_id in rec.picking_ids:
                # people purhcase
                for purchase in rec.people_purchase:
                    self.env['picking.res.partner.purchase'].create({
                        'picking_id': picking_id.id,
                        'partner_id': purchase.partner_id.id
                    })
                # people check
                for check in rec.people_check_id:
                    self.env['picking.res.partner.check'].create({
                        'picking_id': picking_id.id,
                        'partner_id': check.partner_id.id,
                    })
        return res
