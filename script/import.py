import os

path = os.path.join('c:' + os.sep, 'Users', 'xxxx', 'Desktop', 'student-intervention-system', 'student-data.csv')
student_data = pd.read_csv(path)

import sys  
sys.path.insert(0, '/path/to/application/app/folder')

import file

import sys
import os

module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path+"\\nn_webserver")

from employee import motivation_to_work


# or you can

import pandas as pd

df = pd.read_csv (r'Path where the CSV file is stored\File name.csv')
print (df)
