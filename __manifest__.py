# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Tribute Fields',
    'version': '1.0.0',
    'depends': ['base','contacts'],
    'description': "Agrega los campos RUC y LAE a los modelos Company y Partner",
    'license' : "LGPL-3",
    'installable' : True,
    'data': [
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
    ]
}