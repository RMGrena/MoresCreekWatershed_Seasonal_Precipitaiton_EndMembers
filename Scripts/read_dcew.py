# read_dcew.py
import pandas as pd
import numpy as np


def read_and_process():
    dc = pd.read_csv('../Data/02.DCEW_Stream_Isotopes.csv',parse_dates = [2])
    
    
    #remove ID numbers from site names
    dc['Site_no'] = dc.Site_ID.str[3:7]
    dc['Type'] = 'DC'
    dc.head()

    #take out -
    dc = dc.replace(['LR-1'],'LR')
    dc = dc.replace(['MR-1'],'MR')
    dc = dc.replace(['UR-1'],'UR')
    dc = dc.replace(['LG-1'],'LG')
    dc = dc.replace(['C2E-'],'C2E')
    dc = dc.replace(['C2M-'],'C2M')
    dc = dc.replace(['C1W-'],'C1W')
    dc = dc.replace(['C1WS'],'C1WSP')
    dc = dc.replace(['C1E-'],'C1E')
    dc = dc.replace(['MR-2'],'MR')
    dc = dc.replace(['UR-2'],'UR')
    

    # create a list of our conditions to place site_no with elevation
    cond = [
        (dc['Site_no'] == 'LG'),
        (dc['Site_no'] == 'LR'),
        (dc['Site_no'] == 'MR'),
        (dc['Site_no'] == 'UR'),
        (dc['Site_no'] == 'C2M'),
        (dc['Site_no'] == 'C2E'),
        (dc['Site_no'] == 'C1E'),
        (dc['Site_no'] == 'C1WSP'),
        (dc['Site_no'] == 'C1W')        
        ]
    #c1wS needs elevation
    # create a list of the values we want to assign for each condition
    #LG= 1036 C2m= 1143 c2e= 1158 c1w= 1347 c1e= 1335 
    #estimating rose is UR = 1064.5m MR = 1062.5m LR = 1060.5m
    val = [1036, 1060, 1062, 1064, 1143, 1158, 1335, 1344, 1347]
#not sure about C1WSP Guess 1344 due to sampling design coming before C1W
    # create a new column and use np.select to assign values to it using our lists as arguments
    dc['elevation'] = np.select(cond, val)
    
    return dc