from odoo import fields, api, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    ruc = fields.Char('RUC')
    taxpayer_license = fields.Char('LAE')
    municipality = fields.Char('Municipality')
    show_fiscal_fields = fields.Boolean("Show Fiscal Fields", default=True)