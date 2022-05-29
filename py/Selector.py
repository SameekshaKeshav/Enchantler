
# coding: utf-8

#uses cars_engage_2022.csv sample file provided for this mentorship program
#showcases dynamic data filter capabilities to retur the filtered data set to the browser
#data returned via the table tag of html for user freindly rendering the dataset on the browser

import pandas as pd
import sys

file = pd.read_csv("./data/cars_engage_2022.csv")
lowerBudget = int(sys.argv[1])
higherBudget = int(sys.argv[2])
rows=file.loc[(file['Ex_Showroom_Price']<=higherBudget)]
rows1 = rows.loc[(file['Ex_Showroom_Price']>=lowerBudget)]
rows1 = rows1[['Make' , 'Model' , 'Variant','Ex_Showroom_Price']]
rows1.reset_index(drop=True, inplace=True)
f = open("./images/output.txt", 'w')
f.write("<table id='customers'>")
f.write("<tr>"+'<th>Make</th>'+'<th>Model</th>'+'<th>Variant</th>'+'<th>Ex_Showroom_Price</th>'+"</tr>")
for index, row in rows1.iterrows():
    if index > len(rows1):
       break
    else:
       f.write("<tr><td>"+row[0]+"</td><td>"+row[1]+"</td><td>"+row[2]+"</td><td>"+str(row[3])+"</td></tr>")
       index+=1
f.write("</table>")
f.close()
