import pandas as pd
import sys 
import csv 
import os


def find_delimiter(input_file):
   try:
      with open(input_file, 'r') as f:
         dialect = csv.Sniffer().sniff(f.read(10024))
         return dialect.delimiter
   except FileNotFoundError:
      print(f'Error : File "{input_file}" not found  ')
      return None
   
def convert_to_csv(input_file1, input_file2,  delimiter):
   try:
      df1 = pd.read_csv(input_file1, delimiter= delimiter , encoding='windows-1252' , engine='python', quoting=3, header= None)
      df2 = pd.read_csv(input_file2, delimiter= delimiter , encoding='windows-1252' , engine='python', quoting=3 , header= None)
      shape1 = df1.shape[0]
      shape2 = df2.shape[0]
      match_data_file1  = df1 [df1.apply(tuple, 1 ).isin(df2.apply(tuple , 1 ))]
      unmatch_data_file1 = df1[~df1.apply(tuple,1).isin(df2.apply(tuple, 1))]
      match_data_file2  = df2 [df2.apply(tuple, 1 ).isin(df1.apply(tuple , 1 ))]
      unmatch_data_file2 = df2[~df2.apply(tuple,1).isin(df1.apply(tuple, 1))]
  
      shapefile1match = match_data_file1.shape[0]
      shapefile1unmatch = unmatch_data_file1.shape[0]
      shapefile2match = match_data_file2.shape[0]
      shapefile2unmatch = unmatch_data_file2.shape[0]
      unique_records = abs(shapefile1unmatch - shapefile2unmatch)
      with open('output.txt' , 'w') as f :
            print(f'Total No of records in {input_file1} is  {shape1}', file= f)
            print(f'Total No of records in {input_file2} is  {shape2}', file= f)
            print(f'Total No of  mathced records in both files are {shapefile1match} and   {shapefile2match}', file= f)
            print(f'Total No of unmatched records in file1 is {shapefile1unmatch} ', file= f)
            print(f'Total No of unmatched records in file2 is {shapefile2unmatch} ', file= f)
            print(f'Total No. of unique records is {unique_records} ', file = f)

      unmatch_data_file1.to_csv('UnmatchFile1.csv' , index = False, header = None )
      unmatch_data_file2.to_csv('UnmatchFile2.csv', index =False , header =None )

   except Exception as e :
      print(f'Error : input file {input_file1} or {input_file2}  not found "{e}"')

def input_file_csv(input_file):
   outputfile = input_file.split('.' , 1)[0] 
   return outputfile


      

if __name__ == '__main__':
   if(len(sys.argv) != 7):
      print('Usage : python fscript.py --file1 <input_file1> --file2 <input_file2> <delimiter>')
   else:
      input_file1 , input_file2 , delimiter = sys.argv[2], sys.argv[4] , sys.argv[5]
      if delimiter == 'auto':
         delimiter = find_delimiter(input_file1)
      if delimiter:
         convert_to_csv(input_file1, input_file2 ,delimiter)
   print(len(sys.argv))

      
   
      