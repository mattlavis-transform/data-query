import os
import xml.etree.ElementTree as ET
from pathlib import Path
import classes.functions as f


class XpathQueryTaric(object):
    def __init__(self, filename, query_class, query_id, scope):
        self.filename = filename
        self.query_class = query_class
        self.query_id = query_id
        self.scope = scope
        self.register_namespaces()

    def register_namespaces(self):
        self.namespaces = {
            'oub': 'urn:publicid:-:DGTAXUD:TARIC:MESSAGE:1.0',
            'env': 'urn:publicid:-:DGTAXUD:GENERAL:ENVELOPE:1.0'
        }
        for ns in self.namespaces:
            ET.register_namespace(ns, self.namespaces[ns])

    def run_query_measure(self, root):
        ret = []
        self.query = ".//oub:measure[oub:measure.sid = '{item}']/..".format(item=self.query_id)
        for elem in root.findall(self.query, self.namespaces):
            transaction_id = self.get_value(elem, "oub:transaction.id")
            goods_nomenclature_sid = self.get_value(elem, "oub:measure/oub:goods.nomenclature.sid")
            goods_nomenclature_item_id = self.get_value(elem, "oub:measure/oub:goods.nomenclature.item.id")
            validity_start_date = self.get_value(elem, "oub:measure/oub:validity.start.date")
            validity_end_date = self.get_value(elem, "oub:measure/oub:validity.end.date")
            measure_type_id = self.get_value(elem, "oub:measure/oub:measure.type")
            geographical_area_id = self.get_value(elem, "oub:measure/oub:geographical.area")
            filename = Path(self.filename).stem
            obj = (filename, self.query_id, transaction_id, goods_nomenclature_item_id, validity_start_date, validity_end_date, measure_type_id, geographical_area_id, goods_nomenclature_sid)
            ret.append(obj)
        return ret

    def run_query_measure_condition(self, root):
        ret = []
        if self.query_id == "delete":
            self.query = ".//oub:measure.condition/..[oub:update.type = '2']"
        else:
            self.query = ".//oub:measure.condition[oub:measure.condition.sid = '{item}']/..".format(item=self.query_id)

        for elem in root.findall(self.query, self.namespaces):
            transaction_id = self.get_value(elem, "oub:transaction.id")
            measure_sid = self.get_value(elem, "oub:measure.condition/oub:measure.sid")
            measure_condition_sid = self.get_value(elem, "oub:measure.condition/oub:measure.condition.sid")
            condition_code = self.get_value(elem, "oub:measure.condition/oub:condition.code")
            component_sequence_number = self.get_value(elem, "oub:measure.condition/oub:component.sequence.number")
            action_code = self.get_value(elem, "oub:measure.condition/oub:action.code")
            certificate_type_code = self.get_value(elem, "oub:measure.condition/oub:certificate.type.code")
            certificate_code = self.get_value(elem, "oub:measure.condition/oub:certificate.code")
            filename = Path(self.filename).stem
            obj = (filename, self.query_id, transaction_id, measure_sid, measure_condition_sid, condition_code, component_sequence_number, action_code, certificate_type_code, certificate_code)
            ret.append(obj)
        return ret

    def run_query_commodity(self, root):
        ret = []
        self.query = ".//oub:goods.nomenclature[oub:goods.nomenclature.item.id = '{item}']/..".format(item=self.query_id)
        for elem in root.findall(self.query, self.namespaces):
            transaction_id = self.get_value(elem, "oub:transaction.id")
            sid = self.get_value(elem, "oub:goods.nomenclature/oub:goods.nomenclature.sid")
            productline_suffix = self.get_value(elem, "oub:goods.nomenclature/oub:producline.suffix")
            validity_start_date = self.get_value(elem, "oub:goods.nomenclature/oub:validity.start.date")
            validity_end_date = self.get_value(elem, "oub:goods.nomenclature/oub:validity.end.date")
            filename = Path(self.filename).stem
            obj = (filename, self.query_id, sid, productline_suffix, transaction_id, validity_start_date, validity_end_date)
            ret.append(obj)
        return ret

    def run_query_measure_type(self, root):
        ret = []
        self.query = ".//oub:measure[oub:measure.type = '{item}']/..".format(item=self.query_id)
        for elem in root.findall(self.query, self.namespaces):
            transaction_id = self.get_value(elem, "oub:transaction.id")
            measure_sid = self.get_value(elem, "oub:measure.sid")
            goods_nomenclature_sid = self.get_value(elem, "oub:measure/oub:goods.nomenclature.sid")
            goods_nomenclature_item_id = self.get_value(elem, "oub:measure/oub:goods.nomenclature.item.id")
            validity_start_date = self.get_value(elem, "oub:measure/oub:validity.start.date")
            validity_end_date = self.get_value(elem, "oub:measure/oub:validity.end.date")
            measure_type_id = self.get_value(elem, "oub:measure/oub:measure.type")
            geographical_area_id = self.get_value(elem, "oub:measure/oub:geographical.area")
            filename = Path(self.filename).stem
            obj = (filename, self.query_id, transaction_id, measure_sid, goods_nomenclature_item_id, validity_start_date, validity_end_date, measure_type_id, geographical_area_id, goods_nomenclature_sid)
            ret.append(obj)
        return ret

    def run_query_geographical_area(self, root):
        ret = []
        self.query = ".//oub:measure[oub:geographical.area = '{item}']/..".format(item=self.query_id)
        for elem in root.findall(self.query, self.namespaces):
            transaction_id = self.get_value(elem, "oub:transaction.id")
            measure_sid = self.get_value(elem, "oub:measure.sid")
            goods_nomenclature_sid = self.get_value(elem, "oub:measure/oub:goods.nomenclature.sid")
            goods_nomenclature_item_id = self.get_value(elem, "oub:measure/oub:goods.nomenclature.item.id")
            validity_start_date = self.get_value(elem, "oub:measure/oub:validity.start.date")
            validity_end_date = self.get_value(elem, "oub:measure/oub:validity.end.date")
            measure_type_id = self.get_value(elem, "oub:measure/oub:measure.type")
            geographical_area_id = self.get_value(elem, "oub:measure/oub:geographical.area")
            filename = Path(self.filename).stem
            obj = (filename, self.query_id, transaction_id, measure_sid, goods_nomenclature_item_id, validity_start_date, validity_end_date, measure_type_id, geographical_area_id, goods_nomenclature_sid)
            ret.append(obj)
        return ret

    def get_value(self, elem, query):
        obj = elem.find(query, self.namespaces)
        if obj is None:
            return ""
        else:
            return obj.text
