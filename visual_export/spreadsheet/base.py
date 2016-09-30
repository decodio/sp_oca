# -*- coding: utf-8 -*-
from io import BytesIO


class SpreadSheetBase(object):

    document = None
    table = None

    def __init__(self, title):
        self.title = title

    def tofile(self):
        if self.document is None:
            raise Exception('No document found')
        fp = BytesIO()
        self.document.save(fp)
        fp.seek(0)
        data = fp.read()
        fp.close()
        return data

    def AddRow(self, style=None):
        raise Exception('Not implemented')


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
