# zipping and unzipping:
from zipfile import *
f=ZipFile('files.zip','w',ZIP_DEFLATED)
f.write('abc.txt')
f.write('bhargavi.txt')
f.write('emp.csv')
f.write('pretheka.jpg')
f.write('shivaansh.jpg')
f.write('rohinath.dwg')
f.close()
print('zip done ')