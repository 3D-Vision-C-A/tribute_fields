from odoo import models, fields, api, _
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    control_number = fields.Char("Control Number", copy=False)

    @api.constrains("control_number")
    def check_control_number(self):
        for move in self:
            if move.control_number and move.move_type in ['out_invoice','out_refund']:
                try:
                    assert move.control_number.isdigit(), \
                    _("The number of the fiscal correlative must be an entire digit")
                except Exception as e:
                    raise UserError(str(e))