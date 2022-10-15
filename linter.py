import os
import sys
import csv
import glob
from dotenv import load_dotenv


load_dotenv('.env')

log_folder = os.path.join(os.getcwd(), "logs")
log_file = os.path.join(log_folder, "lint_log.csv")
if not os.path.isfile(log_file):
    file = open(log_file, "w+")
    file.close()

file = open(log_file)
csvreader = csv.reader(file)
linted_files = []
for row in csvreader:
    linted_files.append(row[0])
file.close()

folder = os.getenv('DIT_DATA_FOLDER')
glob_path = os.path.join(folder, "*.xml")
files = glob.glob(glob_path)
files = sorted(files)
changed = False
for filename in files:
    base_name = os.path.basename(filename)
    if base_name not in linted_files:
        filename2 = filename.replace(".xml", "_linted.xml")
        lint_script = "xmllint --format '{filename}' > '{filename2}'".format(
            filename=filename,
            filename2=filename2
        )
        os.system(lint_script)
        os.remove(filename)
        os.rename(filename2, filename)
        print("Linting file {filename}".format(filename=base_name))
        linted_files.append(base_name)
        changed = True
        
if changed:
    file = open(log_file, "w+")
    for linted_file in linted_files:
        file.write(linted_file  + "\n")

    file.close()
