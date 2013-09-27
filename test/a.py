# -*- coding: utf-8 -*-
import pyjf
print repr(u'使'.encode('euc-jp'))
print repr(pyjf.sjistoeuc(u'使'.encode('sjis')))
