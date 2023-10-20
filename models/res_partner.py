from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    ruc = fields.Char('RUC', help='Registro Unico de Contribuyente')
    taxpayer_license = fields.Char('N° de icencia', help='Numero de Licencia de Contribuyente')
    ced_rif = fields.Char('Cedula / RIF')
    is_legal_entity = fields.Boolean('Is Legal Entity', default=False)