#!/usr/bin/env python

import glob
import sys
from classes.xpath_query import XpathQuery
from classes.xpath_markdown import XpathMarkdown
import classes.functions as f


f.clear()
if len(sys.argv) < 4:
    ret = f.get_config_variables()
    query_class = ret[1]
    query_id = ret[2]
    scope = ret[0]
else:
    query_class = sys.argv[1]
    query_id = sys.argv[2]
    scope = sys.argv[3]

    query_class = f.cater_for_shortcuts(query_class)
    scope = f.cleanse_scope(scope)

folder = f.get_folder(scope)
files = glob.glob(folder + '/*.xml')
files = sorted(files)
records = []
for filename in files:
    xpq = XpathQuery(filename, query_class, query_id, scope)
    ret = xpq.run_query()
    if ret is not None:
        records += ret

xpm = XpathMarkdown(records, query_class, query_id, scope)
xpm.write_markdown()
xpm.load_in_code()
