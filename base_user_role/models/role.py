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


class res_users_role(osv.Model):
    _name = 'res.users.role'
    _inherits = {'res.groups': 'group_id'}
    _description = "User role"

    _columns = {
        'group_id': fields.many2one(
            'res.groups', required=True, ondelete='cascade',
            readonly=True, string=u"Associated group"),
        'user_ids': fields.many2many(
            'res.users',
            'res_users_role_user_rel',
            'role_id', 'user_id',
            string=u"Users"),
    }

    def create(self, cr, uid, vals, context=None):
        new_id = super(res_users_role, self).create(
            cr, uid, vals, context=context)
        self.update_users(cr, uid, [new_id], context=context)
        return new_id

    def write(self, cr, uid, ids, vals, context=None):
        res = super(res_users_role, self).write(
            cr, uid, ids, vals, context=context)
        self.update_users(cr, uid, ids, context=context)
        return res

    def update_users(self, cr, uid, ids, context=None):
        """Update all the users concerned by the roles identified by `ids`."""
        if context is None:
            context = {}
        user_model = self.pool.get('res.users')
        user_ids = []
        for role in self.browse(cr, uid, ids, context=context):
            user_ids.extend([user.id for user in role.user_ids])
        if user_ids:
            user_model.set_groups_from_roles(
                cr, uid, user_ids, context=context)
        return True
