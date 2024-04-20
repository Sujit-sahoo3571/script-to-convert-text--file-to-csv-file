import pandas as pd 
import csv
import sys 
# import requests

def find_delimiter(input_file):
    try:
        with open(input_file, "r") as f:
            dialect = csv.Sniffer().sniff(f.read(10024))
            return dialect.delimiter
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return None

def convert_to_csv(input_file , delimiter):
    try:
        df = pd.read_csv(input_file, delimiter='ý' , encoding='windows-1252' , engine='python',  quoting=3 )
        outputfile = input_file.split("." , 1 )[0]
        outputfile += '.csv'
        df.to_csv(outputfile , index= None )

    except Exception as e :
        print(f"ERROR :  input file '{input_file}'not found '{e}' ")


    
if __name__ == '__main__':
    if(len(sys.argv ) != 3):
        print('Usage : python script.py <input_file> <delimiter> ' )
    else :
        input_file , delimiter = sys.argv[1] , sys.argv[2]
        
        if delimiter == 'auto':
            delimiter = find_delimiter(input_file)
        if delimiter : 
            convert_to_csv(input_file, delimiter)
