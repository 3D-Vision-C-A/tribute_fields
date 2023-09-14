# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Tribute Fields",
    "version": "1.0.0",
    "depends": ["base", "contacts"],
    "description": """
        Add the necessary fields for the Registry
        of Fiscal Information in other modules.
    """,
    "author": "3DVision C.A.",
    "website": "https://www.3dvisionve.com",
    "license": "LGPL-3",
    "installable": True,
    "data": [
        "views/res_company_view.xml",
        "views/res_partner_view.xml",
    ],
}
