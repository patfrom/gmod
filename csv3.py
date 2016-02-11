import fileinput
import sys
import re
import os
import csv

def replaceAll(file,searchExp,replaceExp):
 for line in fileinput.input(file, inplace=1):
  if searchExp in line:
   line = line.replace(searchExp,replaceExp)
  sys.stdout.write(line)
  
def replace(file, pattern, subst):
 file_handle = open(file, 'r')
 file_string = file_handle.read()
 file_handle.close()
 file_string = (re.sub(pattern, subst, file_string))
 file_handle = open(file, 'w')
 file_handle.write(file_string)
 print file_handle.name+" replaced with pattern: `"+ pattern +"`"
 file_handle.close()

folders = ['1', '2', '3']
for item in range(len(folders)):
 path = '1/'+ folders[item] +'/'
 for file in os.listdir(path):
  print file
  newfilename = file[:-4]+'-done'
  with open(path+newfilename,'wb') as fp:
   m = csv.writer(fp, delimiter=';')
   with open(path+file, 'rb') as plik:
    t = csv.reader(plik, delimiter=';')
   
    for row in t:
     if row[23] == "FRSHTT":
      row.append('Es_hPa')
      row.append('e_hPa')
      row.append('RH')
      row.append('D_hPa')
      row.append('a_gm3')
      #print row
  	
     if row[5] == "TEMP":
      row[5] = "TEMP_C"
     else:
      row[5] = float(row[5])
      row[5] = str(round((row[5] - 32)*5/9, 1))
      #print row[5]
  	
     if row[7] == "DEWP":
      row[7] = "DEWP_C"
     else:
      row[7] = float(row[7])
      row[7] = str(round(((row[7] - 32)*5/9), 1))
      #print row[7]
  	
     if row[15] == "WDSP":
      row[15] = "WDSP_mps"
     else:
      row[15] = float(row[15])
      row[15] = str(round((row[15] * 0.514), 1))
      #print row[15]

      row.append('Es')
      row[24] = float(row[5])
      row[24] = str(round((6.11 * 10 ** (7.5 * row[24] /(237.7 + row[24])) ), 1))
      #print row[24]
  	
      row.append('e')
      row[25] = float(row[7])
      row[25] = str(round( (6.11 * 10 ** (7.5 * row[25] /(237.7 + row[25])) ), 1))
      #print row[25]
  	
      row.append('RH')
      a1 = float(row[24])
      a2 = float(row[25])
      row[26] = str(round((a2/a1*100), 1))
      #print row[26]
  	
      row.append('D')
      b = float(row[25])
      row[27] = str(round((60.9 - b), 1))
      #print row[27]
  	
      row.append('a')
      c = float(row[25])
      d = float(row[5])
      row[28] = str(round(((216.7 * c)/(d + 273)), 1))
      #print row[28]
  
     #print row
     #m.writerow(row)
     m.writerow([row[0],row[2],row[3],row[4],row[5],row[7],row[15],row[24],row[25],row[26],row[27],row[28]])
    print 'edition complete'
  replace(path+newfilename,"\.",",")
