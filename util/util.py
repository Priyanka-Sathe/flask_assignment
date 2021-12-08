import pandas as pd
from util import config as cfg

'''This is a Utility package'''

def extract_csv():
    '''extract_csv is used for extracting CSV and returns a Dataframe.'''
    file_path = cfg.FILE_PATH
    dataframe_new = pd.read_csv(file_path)
    return dataframe_new
    
def query_df(df,k,val):
    '''query_df Queries Dataframe based on parameters like subject,year,author, title and returns result'''
    df.query(k+' == @val', inplace = True)

    col_list = []
   
    for (columnName, columnData) in df.iteritems():
        col_list.append(columnName)
        
    return col_list