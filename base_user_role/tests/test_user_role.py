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


from openerp.tests.common import TransactionCase


class TestUserRole(TransactionCase):

    def setUp(self):
        super(TestUserRole, self).setUp()
        self.imd_model = self.registry('ir.model.data')
        self.user_model = self.registry('res.users')
        self.role_model = self.registry('res.users.role')

        self.user_id = self.user_model.create(
            self.cr, self.uid,
            {'name': u"USER TEST (ROLES)", 'login': 'user_test_roles'})
        self.user_demo_id = self.imd_model.get_object_reference(
            self.cr, self.uid, 'base', 'user_demo')[1]

        # ROLE_1
        self.group_user_id = self.imd_model.get_object_reference(
            self.cr, self.uid, 'base', 'group_user')[1]
        self.group_no_one_id = self.imd_model.get_object_reference(
            self.cr, self.uid, 'base', 'group_no_one')[1]
        vals = {
            'name': u"ROLE_1",
            'group_ids': [6, 0, [self.group_user_id, self.group_no_one_id]],
        }
        self.role1_id = self.role_model.create(self.cr, self.uid, vals)

        # ROLE_2
        self.group_multi_currency_id = self.imd_model.get_object_reference(
            self.cr, self.uid, 'base', 'group_multi_currency')[1]
        self.group_sale_manager_id = self.imd_model.get_object_reference(
            self.cr, self.uid, 'base', 'group_sale_manager')[1]
        vals = {
            'name': u"ROLE_2",
            'group_ids': [6, 0, [self.group_multi_currency_id,
                                 self.group_sale_manager_id]],
        }
        self.role2_id = self.role_model.create(self.cr, self.uid, vals)

    def test_role_1(self):
        role1 = self.role_model.browse(self.cr, self.uid, self.role1_id)
        self.user_model.write(
            self.cr, self.uid, [self.user_id],
            {'role_ids': [(6, 0, [self.role1_id])]})
        user = self.user_model.browse(self.cr, self.uid, self.user_id)
        user_group_ids = sorted(set([group.id for group in user.groups_id]))
        role_group_ids = [group.id for group in role1.group_ids]
        role_group_ids.append(role1.group_id.id)
        role_group_ids = sorted(set(role_group_ids))
        self.assertEqual(user_group_ids, role_group_ids)

    def test_role_2(self):
        role2 = self.role_model.browse(self.cr, self.uid, self.role2_id)
        self.user_model.write(
            self.cr, self.uid, [self.user_id],
            {'role_ids': [(6, 0, [self.role2_id])]})
        user = self.user_model.browse(self.cr, self.uid, self.user_id)
        user_group_ids = sorted(set([group.id for group in user.groups_id]))
        role_group_ids = [group.id for group in role2.group_ids]
        role_group_ids.append(role2.group_id.id)
        role_group_ids = sorted(set(role_group_ids))
        self.assertEqual(user_group_ids, role_group_ids)

    def test_role_1_2(self):
        role1 = self.role_model.browse(self.cr, self.uid, self.role1_id)
        role2 = self.role_model.browse(self.cr, self.uid, self.role2_id)
        self.user_model.write(
            self.cr, self.uid, [self.user_id],
            {'role_ids': [(6, 0, [self.role1_id, self.role2_id])]})
        user = self.user_model.browse(self.cr, self.uid, self.user_id)
        user_group_ids = sorted(set([group.id for group in user.groups_id]))
        role1_group_ids = [group.id for group in role1.group_ids]
        role1_group_ids.append(role1.group_id.id)
        role2_group_ids = [group.id for group in role2.group_ids]
        role2_group_ids.append(role2.group_id.id)
        role_group_ids = sorted(set(role1_group_ids + role2_group_ids))
        self.assertEqual(user_group_ids, role_group_ids)
