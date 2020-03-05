import os
import datetime
import shutil
temp_dir = ["C:\\TEMP",
            ]
ct = datetime.datetime.now()
for i in temp_dir:
    a = os.scandir(i)
    for i in a:
        mod_timestamp = datetime.datetime.fromtimestamp(i.stat().st_mtime)
        if ct - mod_timestamp > datetime.timedelta(14):
            if os.path.isdir(i):
                try:
                    shutil.rmtree(i.path)
                except:
                    pass
            else:
                try:
                    os.remove(i.path)
                except:
                    pass






