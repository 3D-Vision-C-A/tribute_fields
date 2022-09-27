from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    ruc = fields.Char('RUC', help='Registro Unico de Contribuyente')
    taxpayer_license = fields.Char('N° Licencia', help='Numero de Licencia de Contribuyente')