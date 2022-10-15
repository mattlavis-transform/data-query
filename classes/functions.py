import inquirer
import os
from os import system, name
from colorama import init, Fore, Back, Style
from dotenv import load_dotenv


def cater_for_shortcuts(query_class):
    if query_class in ("m", "measures"):
        query_class = "measure"
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
            "Measures",
            "Measure conditions",
            "Measure types",
            "Commodities",
            "Geographical areas",
            "Commodity measures"
            ]),
        inquirer.Text("entity", message="What entity are you looking for?")
    ]

    answers = inquirer.prompt(questions)
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
        "Measures": "measure",
        "Measure conditions": "measure_condition",
        "Measure types": "measure_type",
        "Commodities": "commodity",
        "Geographical areas": "geographical_area",
        "Commodity measures": "commodity_measure"
    }
    return scopes[s]

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system("printf '\33c\e[3J'")

