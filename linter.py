import os
import sys
import glob
from dotenv import load_dotenv


load_dotenv('.env')
folder = os.getenv('DIT_DATA_FOLDER')
glob_path = os.path.join(folder, "*.xml")
files = glob.glob(glob_path)
files = sorted(files)
for filename in files:
    base_name = os.path.basename(filename)
    filename2 = filename.replace(".xml", "_linted.xml")
    lint_script = "xmllint --format '{filename}' > '{filename2}'".format(
        filename=filename,
        filename2=filename2
    )
    os.system(lint_script)
    os.remove(filename)
    os.rename(filename2, filename)
    print("Linting file {filename}".format(filename=base_name))
