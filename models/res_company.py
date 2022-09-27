from odoo import fields, api, models

class ResCompany(models.Model):
    _inherit = 'res.company'

    ruc = fields.Char('RUC', help='Registro Unico de Contribuyente')
    taxpayer_license = fields.Char('N° de Licencia',help='Numero de Licencia del Contribuyente')