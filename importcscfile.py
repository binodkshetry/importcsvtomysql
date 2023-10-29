How to import a CSV file into a MySQL database using python script?
Using iris data, we will learn how to import a CSV file into a MySQL database using python script.
_______________________________________________________________________________________________________

import pandas as pd
irisData = pd.read_csv('https://github.com/Muhd-Shahid/Write-Raw-File-into-Database-Server/raw/main/iris.csv', index_col=False)
irisData.head()
