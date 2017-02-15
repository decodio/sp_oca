# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.addons.list_multiheader.base import MULTIHEADER_VIEW


class IrUiView(osv.Model):
    _inherit = 'ir.ui.view'

    def get_export_header(self, cr, uid, doc, obj, **kwargs):
        if hasattr(obj, 'get_export_header'):
            return obj.get_export_header(cr, uid, doc, **kwargs)
        cellfilled = []
        if kwargs.get('view_type') == MULTIHEADER_VIEW[0]:
            for header in kwargs.get('headers'):
                row = doc.AddRow()
                for c in header:
                    nextcell = (row.number, row.nextcell)
                    while nextcell in cellfilled:
                        cellfilled.remove(nextcell)
                        row.AddStringCell('')
                        nextcell = (row.number, row.nextcell)
                    cell = row.AddStringCell(unicode(c['string']),
                                             rowspan=c['rowspan'],
                                             colspan=c['colspan'])
                    if c['rowspan'] > 1:
                        for rowspan in range(c['rowspan'] - 1):
                            cellfilled.append(
                                (row.number + rowspan + 1, cell.number))
        else:
            super(IrUiView, self).get_export_header(cr, uid, doc, obj, **kwargs)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
