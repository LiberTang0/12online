# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2019-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

from odoo import api, fields, models, _

class CrmLead(models.Model):
    _inherit = "crm.lead"
 

    base_currency_id = fields.Many2one('res.currency', default=lambda self: self.oppoutnity_id.company_id.currency_id.id)
   


@api.onchange('planned_revenue', 'oppoutnity_id.currency_id')
def compute_amount_in_base_currency(self):
    company_currency = self.oppoutnity_id.company_id.currency_id
    for l in self:
        amount_in_base = l.currency_id.compute(l.price_subtotal, company_currency)
        l.amount_in_base = amount_in_base

amount_in_base = fields.Float('Base Amount', readonly=True, compute='compute_amount_in_base_currency')
