import inquirer
import os
from os import system, name
from colorama import init, Fore, Back, Style
from dotenv import load_dotenv


def cater_for_shortcuts(query_class):
    if query_class in ("m", "measures"):
        query_class = "measure"
    if query_class in ("mq"):
        query_class = "measure_quota"
    elif query_class in ("mc", "conditions"):
        query_class = "measure_condition"
    elif query_class in ("c", "commodities"):
        query_class = "commodity"
    elif query_class in ("mt", "measure_types"):
        query_class = "measure_type"
    elif query_class in ("geo", "geography", "geographical_areas", "g", "geographical_area_id"):
        query_class = "geographical_area"
    elif query_class in ("cm", "mc", "measure_commodity"):
        query_class = "commodity_measure"
    elif query_class in ("q", "quotas"):
        query_class = "quota"
    return query_class

def cleanse_scope(scope):
    if scope in ("eu", "xi"):
        scope = "tgb"
    elif scope in ("uk"):
        scope = "dit"
    elif scope in ("cds"):
        scope = "cds"
    return scope

def get_folder(scope):
    load_dotenv('.env')
    if scope == "dit":
        folder = os.getenv('DIT_DATA_FOLDER')
    elif scope == "tgb":
        folder = os.getenv('TGB_DATA_FOLDER')
    else:
        folder = os.getenv('CDS_DATA_FOLDER')
    return folder

def parse_date(d):
    d2 = d[6:8] + "/" + d[4:6] + "/" + d[0:4]
    return (d2)

def get_nodes(path):
    pass

def xml_to_xlsx_filename(filename):
    parts = filename.split("T")
    part0 = parts[0]
    parts = part0.split("-")
    part1 = parts[1]
    excel_filename = "CDS updates " + part1[0:4] + "-" + part1[4:6] + "-" + part1[6:] + ".xlsx"
    return (excel_filename)

def get_config_variables():
    messages = {
        "Measures": "Enter the SID of the measure",
        "Measure conditions": "Enter the SID of the measure condition",
        "Measure types": "Enter the 3-character ID of the measure type",
        "Commodities": "Enter the 10-digit commodity code",
        "Geographical areas": "Enter the 2- or 4-digit ID of the geographical area",
        "Commodity measures": "Not sure"
    }
    questions = [
        inquirer.List("scope", carousel=True, message="Look in which data set?", choices=[
            "DIT data files",
            "CDS data files",
            "EU TGB data files"
        ]),
        inquirer.List("query_class", carousel=True, message="Look in {scope} for which type of data?", choices=[
            "Measures by SID",
            "Measures by quota order number",
            "Measure conditions",
            "Measure types",
            "Commodities",
            "Geographical areas",
            "Commodity measures",
            "Quotas"
        ]),
        inquirer.Text("entity", message="What entity are you looking for?")
    ]

    inquirer_theme = {
        "Question": {
            "mark_color": "yellow",
            "brackets_color": "normal"
        },
        "List": {
            "selection_color": "orchid1",
            "selection_cursor": ">"
        }
    }

    answers = inquirer.prompt(questions, theme=inquirer.themes.load_theme_from_dict(inquirer_theme))
    scope = get_scope_from_enquirer(answers["scope"])
    query_class = get_query_class_from_enquirer(answers["query_class"])
    ret = (
        scope,
        query_class,
        answers["entity"]
    )
    return ret

def get_scope_from_enquirer(s):
    scopes = {
        "CDS data files": "cds",
        "DIT data files": "dit",
        "EU TGB data files": "tgb"
    }
    return scopes[s]

def get_query_class_from_enquirer(s):
    scopes = {
        "Measures by SID": "measure",
        "Measures by quota order number": "measure_quota",
        "Measure conditions": "measure_condition",
        "Measure types": "measure_type",
        "Commodities": "commodity",
        "Geographical areas": "geographical_area",
        "Commodity measures": "commodity_measure",
        "Quotas": "quota"
    }
    return scopes[s]

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system("printf '\33c\e[3J'")

def get_operation_type(value, scope):
    if scope == "taric":
        lookups = {
            "1": "Update",
            "2": "Delete",
            "3": "Insert"
        }
    else:
        lookups = {
            "U": "Update",
            "D": "Delete",
            "C": "Insert"
        }
    return lookups[value]
