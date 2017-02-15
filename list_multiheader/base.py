# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.tools.translate import _
from openerp.tools.safe_eval import safe_eval
#from openerp.addons.base.ir.ir_actions import VIEW_TYPES
from lxml import etree
from logging import getLogger


_logger = getLogger(__name__)
#VIEW_TYPE = ('list_multiheader', _('List multi header'))
#VIEW_TYPES.append(VIEW_TYPE)


from openerp import fields, models
from openerp import api

def valid_node_group(node):
    res = True
    if node.attrib.get('string', None) is None:
        _logger.error("Attribute 'string' missing in the group")
        res = False

    if not node.getchildren():
        _logger.error('The group must have children')
        res = False

    if not valid_type_list_multiheader(node):
        res = False

    return res


def valid_node_field(node, fromgroup=True):
    res = True
    if fromgroup:
        if node.attrib.get('invisible', None) is not None:
            _logger.error("Attribute 'invisible' on the field in one group are not allowed")
            res = False
        if node.attrib.get('attrs', None) is not None:
            attrs = safe_eval(node.attrib['attrs'])
            if attrs.get('invisible', None) is not None:
                _logger.error(
                    "Attribute 'invisible' in attrs on the field in one group are not allowed")
                res = False

    if node.attrib.get('name', None) is None:
        _logger.error("Attribute 'name' missing in the field")
        res = False

    if node.getchildren():
        _logger.error('The field does\'t have children')
        res = False
    return res


def valid_node_button(node):
    res = True
    if node.attrib.get('string', None) is None:
        _logger.error("Attribute 'string' missing in the button")
        res = False

    if node.getchildren():
        _logger.error('The button does\'t have children')
        res = False
    return res


def valid_type_list_multiheader(arch, fromgroup=True):
    res = True
    for node in arch.getchildren():
        if node.tag == 'group':
            if not valid_node_group(node):
                res = False
        elif node.tag == 'field':
            if not valid_node_field(node, fromgroup=fromgroup):
                res = False
        elif node.tag == 'button':
            if not valid_node_button(node):
                res = False
        else:
            _logger.error(
                'the tag %r are not allow in the xml arch' % node.tag)
            res = False
    return res

MULTIHEADER_VIEW = ('list_multiheader', _('List multi header'))


class IrUiView(models.Model):
    _inherit = 'ir.ui.view'

    @api.model
    def _setup_fields(self):
        """Hack due since the field 'type' is not defined with the new api.
        """
        cls = type(self)
        type_selection = cls._fields['type'].selection
        if MULTIHEADER_VIEW not in type_selection:
            tmp = list(type_selection)
            tmp.append(MULTIHEADER_VIEW)
            cls._fields['type'].selection = tuple(set(tmp))
        super(IrUiView, self)._setup_fields()

    """
    def __init__(self, pool, cr):
        res = super(IrUiView, self).__init__(pool, cr)
        select = [k for k, v in self._columns['type'].selection]
        if VIEW_TYPE[0] not in select:
            self._columns['type'].selection.append(VIEW_TYPE)
        return res
    """

    def _check_xml_list_multiheader(self, cr, uid, ids, context=None):
        domain = [
            ('id', 'in', ids),
            ('type', '=', MULTIHEADER_VIEW[0]),
        ]
        view_ids = self.search(cr, uid, domain, context=context)
        for view in self.browse(cr, uid, view_ids, context=context):
            fvg = self.pool.get(view.model).fields_view_get(
                cr, uid, view_id=view.id, view_type=view.type, context=context)
            view_arch_utf8 = fvg['arch']
            view_docs = [etree.fromstring(view_arch_utf8)]
            if view_docs[0].tag == 'data':
                view_docs = view_docs[0]
            for view_arch in view_docs:
                # return True # TODO: tmp
                if not valid_type_list_multiheader(view_arch, fromgroup=False):
                    return False

        return True

    _constraints = [
        (
            _check_xml_list_multiheader,
            'Invalide XML for list_multiheader view architecture',
            ['arch'],
        ),
    ]

