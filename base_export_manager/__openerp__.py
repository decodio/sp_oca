# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería S.L. - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Manage model export profiles",
    'category': 'Personalization',
    'version': '8.0.2.0.1',
    'depends': [
        'web',
    ],
    'data': [
        'data/ir_exports_data.xml',
        'views/assets.xml',
        'views/ir_exports_view.xml',
    ],
    'qweb': [
        "static/src/xml/base.xml",
    ],
    'author': 'Antiun Ingeniería S.L., '
              'Tecnativa, '
              'Odoo Community Association (OCA)',
    'website': 'http://www.antiun.com',
    'license': 'AGPL-3',
    'installable': True,
}
