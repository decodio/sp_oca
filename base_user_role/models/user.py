# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 ABF OSIELL SARL (http://osiell.com).
#                       Sebastien Alix <contact@osiell.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields


class res_users(osv.Model):
    _inherit = 'res.users'

    _columns = {
        'role_ids': fields.many2many(
            'res.users.role',
            'res_users_role_user_rel',
            'user_id', 'role_id',
            string=u"Roles"),
    }

    def create(self, cr, uid, vals, context=None):
        new_id = super(res_users, self).create(
            cr, uid, vals, context=context)
        self.set_groups_from_roles(cr, uid, [new_id], context=context)
        return new_id

    def write(self, cr, uid, ids, vals, context=None):
        res = super(res_users, self).write(
            cr, uid, ids, vals, context=context)
        self.set_groups_from_roles(cr, uid, ids, context=context)
        return res

    def set_groups_from_roles(self, cr, uid, ids, context=None):
        """Set (replace) the groups following the roles defined on users.
        If no role is defined on the user, its groups are let untouched.
        """
        if context is None:
            context = {}
        for user in self.browse(cr, uid, ids, context=context):
            if not user.role_ids:
                continue
            group_ids = []
            for role in user.role_ids:
                group_ids.append(role.group_id.id)
                group_ids.extend([group.id for group in role.implied_ids])
            if group_ids:
                group_ids = list(set(group_ids))    # Remove duplicates IDs
                vals = {
                    'groups_id': [(6, 0, group_ids)],
                }
                super(res_users, self).write(
                    cr, uid, [user.id], vals, context=context)
        return True
