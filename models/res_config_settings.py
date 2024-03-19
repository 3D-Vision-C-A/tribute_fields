from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
  _inherit = 'res.config.settings'

  show_fiscal_fields = fields.Boolean(related="company_id.show_fiscal_fields", readonly=False)