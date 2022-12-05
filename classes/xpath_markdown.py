import subprocess
import os
import xml.etree.ElementTree as ET
from pathlib import Path


class XpathMarkdown(object):
    def __init__(self, records, query_class, query_id, scope):
        self.records = records
        self.query_class = query_class
        self.query_id = query_id
        self.scope = scope
        self.markdown = ""
        self.make_folders()
        self.get_filename()

    def make_folders(self):
        resources_folder = os.path.join(os.getcwd(), "resources")
        queries_folder = os.path.join(resources_folder, "queries")
        dit_folder = os.path.join(queries_folder, "dit")
        tgb_folder = os.path.join(queries_folder, "tgb")
        cds_folder = os.path.join(queries_folder, "cds")

        if self.scope == "dit":
            parent_folder = dit_folder
        elif self.scope == "cds":
            parent_folder = cds_folder
        else:
            parent_folder = tgb_folder

        self.measures_folder = os.path.join(parent_folder, "measures")
        self.measure_quotas_folder = os.path.join(parent_folder, "measure_quotas")
        self.measure_conditions_folder = os.path.join(parent_folder, "measure_conditions")
        self.commodities_folder = os.path.join(parent_folder, "commodities")
        self.measure_types_folder = os.path.join(parent_folder, "measure_types")
        self.geographical_areas_folder = os.path.join(parent_folder, "geographical_areas")
        self.commodity_measures_folder = os.path.join(parent_folder, "commodity_measures")
        self.quotas_folder = os.path.join(parent_folder, "quotas")

        self.make_folder(queries_folder)
        self.make_folder(dit_folder)
        self.make_folder(cds_folder)
        self.make_folder(tgb_folder)

        self.make_folder(self.measures_folder)
        self.make_folder(self.measure_quotas_folder)
        self.make_folder(self.measure_conditions_folder)
        self.make_folder(self.commodities_folder)
        self.make_folder(self.measure_types_folder)
        self.make_folder(self.geographical_areas_folder)
        self.make_folder(self.commodity_measures_folder)
        self.make_folder(self.quotas_folder)

    def make_folder(self, folder):
        try:
            os.mkdir(folder)
        except Exception as e:
            pass

    def get_filename(self):
        self.filename = "{qc}_{qid}.md".format(qc=self.query_class, qid=self.query_id)
        if self.query_class == "measure":
            self.filepath = os.path.join(self.measures_folder, self.filename)
        elif self.query_class == "measure_quota":
            self.filepath = os.path.join(self.measure_quotas_folder, self.filename)
        elif self.query_class == "measure_condition":
            self.filepath = os.path.join(self.measure_conditions_folder, self.filename)
        elif self.query_class == "commodity":
            self.filepath = os.path.join(self.commodities_folder, self.filename)
        elif self.query_class == "measure_type":
            self.filepath = os.path.join(self.measure_types_folder, self.filename)
        elif self.query_class == "geographical_area":
            self.filepath = os.path.join(self.geographical_areas_folder, self.filename)
        elif self.query_class == "commodity_measure":
            self.filepath = os.path.join(self.commodity_measures_folder, self.filename)
        elif self.query_class == "quota":
            self.filepath = os.path.join(self.quotas_folder, self.filename)

    def write_markdown(self):
        self.get_unique_filenames()
        if self.query_class == "measure":
            self.write_markdown_measure()
        elif self.query_class == "measure_quota":
            self.write_markdown_measure_quotas()
        elif self.query_class == "measure_condition":
            self.write_markdown_measure_condition()
        elif self.query_class == "commodity":
            self.write_markdown_commodity()
        elif self.query_class == "measure_type":
            self.write_markdown_measure_type()
        elif self.query_class == "geographical_area":
            self.write_markdown_geographical_area()
        elif self.query_class == "commodity_measure":
            self.write_markdown_commodity_measure()
        elif self.query_class == "quota":
            self.write_markdown_quota()

    def write_markdown_measure(self):
        self.markdown += "# Instances of measure SID {item}\n\n".format(item=self.query_id)
        self.markdown += "## Files containing item\n\n"
        for filename in self.unique_filenames:
            self.markdown += "- {item}\n".format(item=filename)

        self.markdown += "\n## Instances\n\n"
        for record in self.records:
            self.markdown += "### {item}\n\n".format(item=record[0])
            self.markdown += "- Transaction ID = {item}\n".format(item=record[2])
            self.markdown += "- Commodity code = {item}\n".format(item=record[3])
            self.markdown += "- Start date = {item}\n".format(item=record[4])
            self.markdown += "- End date = {item}\n".format(item=record[5])
            self.markdown += "- Measure type ID = {item}\n".format(item=record[6])
            self.markdown += "- Geographical area ID = {item}\n".format(item=record[7])
            self.markdown += "- Goods nomenclature SID = {item}\n".format(item=record[8])
            self.markdown += "- Quota order number = {item}\n".format(item=record[9])
            self.markdown += "- Operation type = {item}\n\n".format(item=record[10])

        self.write_report()

    def write_markdown_measure_quotas(self):
        self.markdown += "# Instances of measures assigned to quota {item}\n\n".format(item=self.query_id)
        self.markdown += "## Files containing item\n\n"
        for filename in self.unique_filenames:
            self.markdown += "- {item}\n".format(item=filename)

        self.markdown += "\n## Instances\n\n"
        for record in self.records:
            self.markdown += "### {item}\n\n".format(item=record[0])
            self.markdown += "- Transaction ID = {item}\n".format(item=record[2])
            self.markdown += "- Measure SID = {item}\n".format(item=record[3])
            self.markdown += "- Commodity code = {item}\n".format(item=record[4])
            self.markdown += "- Start date = {item}\n".format(item=record[5])
            self.markdown += "- End date = {item}\n".format(item=record[6])
            self.markdown += "- Measure type ID = {item}\n".format(item=record[7])
            self.markdown += "- Geographical area ID = {item}\n".format(item=record[8])
            self.markdown += "- Goods nomenclature SID = {item}\n".format(item=record[9])
            self.markdown += "- Quota order number = {item}\n".format(item=record[10])
            self.markdown += "- Operation type = {item}\n\n".format(item=record[11])

        self.write_report()

    def write_markdown_measure_condition(self):
        self.markdown += "# Instances of measure condition SID {item}\n\n".format(item=self.query_id)
        self.markdown += "## Files containing item\n\n"
        for filename in self.unique_filenames:
            self.markdown += "- {item}\n".format(item=filename)

        self.markdown += "\n## Instances\n\n"
        unique_measures = []
        unique_conditions = []
        conditions_and_measures = []
        for record in self.records:
            self.markdown += "### {item}\n\n".format(item=record[0])
            self.markdown += "- Transaction ID = {item}\n".format(item=record[2])
            self.markdown += "- Measure SID = {item}\n".format(item=record[3])
            self.markdown += "- Measure condition SID = {item}\n".format(item=record[4])
            self.markdown += "- Condition code = {item}\n".format(item=record[5])
            self.markdown += "- Component sequence number = {item}\n".format(item=record[6])
            self.markdown += "- Action code = {item}\n".format(item=record[7])
            self.markdown += "- Certificate type code = {item}\n".format(item=record[8])
            self.markdown += "- Certificate code = {item}\n".format(item=record[9])
            self.markdown += "- Operation type = {item}\n\n".format(item=record[10])

            combined = record[4] + " : " + record[3]
            if record[3] not in unique_measures:
                unique_measures.append(record[3])

            unique_conditions.append(record[4])
            conditions_and_measures.append(combined)

        self.markdown += "Measures\n\n"
        self.markdown += ",".join(unique_measures)

        self.markdown += "\n\nMeasure conditions\n\n"
        self.markdown += ",".join(unique_conditions)

        self.markdown += "\n\nMeasures and conditions\n\n"
        self.markdown += "\n".join(conditions_and_measures)

        self.write_report()

    def write_markdown_commodity(self):
        self.markdown += "# Instances of commodity code {item}\n\n".format(item=self.query_id)
        self.markdown += "## Files containing item\n\n"
        for filename in self.unique_filenames:
            self.markdown += "- {item}\n".format(item=filename)

        self.markdown += "\n## Instances\n\n"
        for record in self.records:
            self.markdown += "### {filename}\n\n".format(filename=record[0])
            self.markdown += "- Transaction ID = {item}\n".format(item=record[4])
            self.markdown += "- Commodity code = {item}\n".format(item=record[1])
            self.markdown += "- Product Line Suffix = {item}\n".format(item=record[3])
            self.markdown += "- Goods nomenclature SID = {item}\n".format(item=record[2])
            self.markdown += "- Start date = {item}\n".format(item=record[5])
            self.markdown += "- End date = {item}\n".format(item=record[6])
            self.markdown += "- Operation type = {item}\n\n".format(item=record[7])

        self.write_report()

    def write_markdown_measure_type(self):
        self.markdown += "# Instances of measure type {item}\n\n".format(item=self.query_id)
        self.markdown += "## Files containing item\n\n"
        for filename in self.unique_filenames:
            self.markdown += "- {item}\n".format(item=filename)

        self.markdown += "\n## Instances\n\n"
        for record in self.records:
            self.markdown += "### {item}\n\n".format(item=record[0])
            self.markdown += "- Transaction ID = {item}\n".format(item=record[2])
            self.markdown += "- Measure SID = {item}\n".format(item=record[3])
            self.markdown += "- Commodity code = {item}\n".format(item=record[4])
            self.markdown += "- Start date = {item}\n".format(item=record[5])
            self.markdown += "- End date = {item}\n".format(item=record[6])
            self.markdown += "- Measure type ID = {item}\n".format(item=record[7])
            self.markdown += "- Geographical area ID = {item}\n".format(item=record[8])
            self.markdown += "- Goods nomenclature SID = {item}\n".format(item=record[9])
            self.markdown += "- Operation type = {item}\n\n".format(item=record[10])

        self.write_report()

    def write_markdown_geographical_area(self):
        self.markdown += "# Instances of measures applied to geographical area {item}\n\n".format(item=self.query_id)
        self.markdown += "## Files containing item\n\n"
        for filename in self.unique_filenames:
            self.markdown += "- {item}\n".format(item=filename)

        self.markdown += "\n## Instances\n\n"
        for record in self.records:
            self.markdown += "### {item}\n\n".format(item=record[0])
            self.markdown += "- Transaction ID = {item}\n".format(item=record[2])
            self.markdown += "- Measure SID = {item}\n".format(item=record[3])
            self.markdown += "- Commodity code = {item}\n".format(item=record[4])
            self.markdown += "- Start date = {item}\n".format(item=record[5])
            self.markdown += "- End date = {item}\n".format(item=record[6])
            self.markdown += "- Measure type ID = {item}\n".format(item=record[7])
            self.markdown += "- Geographical area ID = {item}\n".format(item=record[8])
            self.markdown += "- Goods nomenclature SID = {item}\n".format(item=record[9])
            self.markdown += "- Order number = {item}\n".format(item=record[10])
            self.markdown += "- Operation type = {item}\n\n".format(item=record[11])

        self.write_report()

    def write_markdown_commodity_measure(self):
        self.markdown += "# Instances of measures applied to commodity code {item}\n\n".format(item=self.query_id)
        self.markdown += "## Files containing item\n\n"
        for filename in self.unique_filenames:
            self.markdown += "- {item}\n".format(item=filename)

        self.markdown += "\n## Instances\n\n"
        for record in self.records:
            self.markdown += "### {item}\n\n".format(item=record[0])
            self.markdown += "- Transaction ID = {item}\n".format(item=record[2])
            self.markdown += "- Measure SID = {item}\n".format(item=record[3])
            self.markdown += "- Commodity code = {item}\n".format(item=record[4])
            self.markdown += "- Start date = {item}\n".format(item=record[5])
            self.markdown += "- End date = {item}\n".format(item=record[6])
            self.markdown += "- Measure type ID = {item}\n".format(item=record[7])
            self.markdown += "- Geographical area ID = {item}\n".format(item=record[8])
            self.markdown += "- Goods nomenclature SID = {item}\n".format(item=record[9])
            self.markdown += "- Operation type = {item}\n\n".format(item=record[10])

        self.write_report()

    def write_markdown_quota(self):
        self.markdown += "# Instances of quota order number {item}\n\n".format(item=self.query_id)
        self.markdown += "## Files containing item\n\n"
        for filename in self.unique_filenames:
            self.markdown += "- {item}\n".format(item=filename)

        self.markdown += "\n## Instances\n\n"
        for record in self.records:
            self.markdown += "### {item}\n\n".format(item=record[0])
            self.markdown += "- Transaction ID = {item}\n".format(item=record[2])
            self.markdown += "- Quota order number SID = {item}\n".format(item=record[3])
            self.markdown += "- Start date = {item}\n".format(item=record[4])
            self.markdown += "- End date = {item}\n".format(item=record[5])
            self.markdown += "- Operation type = {item}\n\n".format(item=record[6])

        self.write_report()

    def get_unique_filenames(self):
        self.unique_filenames = []
        for record in self.records:
            if record[0] not in self.unique_filenames:
                self.unique_filenames.append(record[0])

    def write_report(self):
        f = open(self.filepath, "w")
        f.write(self.markdown)
        f.close()

    def load_in_code(self):
        code_call = "code -r '{data_file}'".format(data_file=self.filepath)
        os.system(code_call)
