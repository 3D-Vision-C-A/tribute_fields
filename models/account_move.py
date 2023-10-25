from odoo import models, fields, api, _
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    control_number = fields.Char("Control Number", copy=False)
    fiscal_check = fields.Boolean("Is Fiscal", default=False, copy=False)
    correlative_prefix = fields.Char("Correlative prefix", copy=False)
    correlative_number = fields.Char("Correlative Number", copy=False)
    fiscal_correlative = fields.Char(
        "Fiscal Correlative",
        compute="_compute_fiscal_correlative",
        store=True,
        copy=False,
    )

    @api.depends("correlative_prefix", "correlative_number")
    def _compute_fiscal_correlative(self):
        for record in self:
            if record.fiscal_check and record.correlative_number:
                number_format = (
                    "0" * (8 - len(record.correlative_number))
                    + record.correlative_number
                )
                record.fiscal_correlative = (
                    "-".join([record.correlative_prefix, number_format])
                    if record.correlative_prefix
                    else number_format
                )
            else:
                record.fiscal_correlative = False

    @api.onchange("fiscal_check")
    def onchange_fiscal_check(self):
        if self.fiscal_check:
            moves = self.env["account.move"].search(
                [
                    ("fiscal_check", "=", True),
                    ("move_type", "=", self.move_type),
                    ("company_id", "=", self.company_id.id),
                ]
            )

            control_numbers = moves.mapped(lambda m: int(m.control_number)) or [
                0
            ]
            correlatives = moves.mapped(
                lambda m: int(m.correlative_number)
            ) or [0]
            prefix = moves[0].correlative_prefix if moves else False

            self.control_number = self.control_number or str(
                max(control_numbers) + 1
            )

            self.correlative_number = self.correlative_number or str(
                max(correlatives) + 1
            )

            self.correlative_prefix = self.correlative_prefix or prefix
        else:
            self.control_number = False
            self.correlative_prefix = False
            self.correlative_number = False

    @api.constrains("control_number")
    def check_control_number(self):
        for move in self:
            if move.control_number and move.move_type in [
                "out_invoice",
                "out_refund",
            ]:
                try:
                    assert move.control_number.isdigit(), _(
                        "The number of the fiscal correlative must be an entire digit"
                    )
                except Exception as e:
                    raise UserError(str(e))
