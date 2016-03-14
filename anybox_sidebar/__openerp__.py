# ==============================================================================
#
#    Anybox Sidebar module for OpenERP
#    Copyright (C) 2015 ANYBOX (<http://www.anybox.fr>)
#
#    This file is a part of paybox
#
#    paybox is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License v3 or later
#    as published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    paybox is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License v3 or later for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    v3 or later along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
# ==============================================================================

{
    'name': 'Anybox Sidebar',
    'version': '0.1',
    'sequence': 150,
    'category': 'Custom',
    'description': """Anybox Sidebar Module""",
    'author': 'Anybox',
    'website': 'www.anybox.fr',
    'depends': [
        'web',
    ],
    'data': [
    ],
    'demo_xml': [
    ],
    'init_xml': [
    ],
    'css': [],
    'js': ['static/src/js/views.js'],
    'icon': '',
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
    'post_load': None,
    }
