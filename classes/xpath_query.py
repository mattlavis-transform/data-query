import sys
import os
import xml.etree.ElementTree as ET
from pathlib import Path
from classes.xpath_query_cds import XpathQueryCds
from classes.xpath_query_taric import XpathQueryTaric


class XpathQuery(object):
    def __init__(self, filename, query_class, query_id, scope):
        self.filename = filename
        self.query_class = query_class
        self.query_id = query_id
        self.scope = scope
        self.get_query_tool()

    def get_query_tool(self):
        if self.scope == "cds":
            self.query_tool = XpathQueryCds(self.filename, self.query_class, self.query_id, self.scope)
        else:
            self.query_tool = XpathQueryTaric(self.filename, self.query_class, self.query_id, self.scope)

    def run_query(self):
        try:
            root = ET.parse(self.filename)
        except Exception as e:
            print(self.filename)
            sys.exit()
        if self.query_class == "measure":
            ret = self.query_tool.run_query_measure(root)
        elif self.query_class == "measure_condition":
            ret = self.query_tool.run_query_measure_condition(root)
        elif self.query_class == "commodity":
            ret = self.query_tool.run_query_commodity(root)
        elif self.query_class == "measure_type":
            ret = self.query_tool.run_query_measure_type(root)
        elif self.query_class == "geographical_area":
            ret = self.query_tool.run_query_geographical_area(root)
        elif self.query_class == "commodity_measure":
            ret = self.query_tool.run_query_commodity_measure(root)
        return ret
