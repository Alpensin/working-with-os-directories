from os.path import basename
from datetime import date
from shutil import copy

source_path = r""
target_path = r""
target_file = target_path+"\ "+str(date.today())+" "+basename(source_path)
copy(source_path, target_file)
