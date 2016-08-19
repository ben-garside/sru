# get path to template
# get content and apply variables
# write it to sru.xml
# execure the run command to the exe file with install param
# ...\sru.exe install
from optparse import OptionParser

from sru_service import main

parser = OptionParser()
parser.add_option("-a", "--action", dest="action", help="action, usually setup", default=None)

(options, args) = parser.parse_args()

ACTION = options.action

if ACTION == "setup":
    return main.setup()

