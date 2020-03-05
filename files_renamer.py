import os, re

j=1
for i in os.scandir():
    if re.match(r"._. handy", i.name):
        newname = re.sub(r"._. handy", "4_%d handy" % j, i.name )
        os.rename(i.name, newname)
        j+=1