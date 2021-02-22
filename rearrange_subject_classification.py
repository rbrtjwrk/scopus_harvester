import pandas as pd

def rearrange_subject_classification(dataframe):
    dataframe=dataframe.copy()
    jt_col_idx=dataframe.columns.get_loc("Journal_Title")
    cs_col_idx=dataframe.columns.get_loc("Subject_Classification")
    row_idx=-1
    for row in dataframe.itertuples():
        row_idx+=1
        if len(row.Subject_Classification) > 1:
            border_1=sum(dataframe.iloc[:row_idx, jt_col_idx]==row.Journal_Title)
            border_2=sum(dataframe.iloc[row_idx:, jt_col_idx]==row.Journal_Title)-1
            dataframe.iloc[row_idx, cs_col_idx]=row.Subject_Classification[border_1:(len(row.Subject_Classification)-border_2)]
    return dataframe   
