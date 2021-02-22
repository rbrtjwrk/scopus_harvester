import pandas as pd

def multiply_journals(dataframe, alphabetical_order=True):
    for row in dataframe.itertuples():
        multiply_by=len(row.Subject_Classification)
        if multiply_by > 1:
            dataframe=dataframe.append([row] * (multiply_by-1), sort=False)
    if alphabetical_order==True:
        dataframe=dataframe.sort_values(by="Journal_Title")
    dataframe=dataframe.reset_index()
    dataframe=dataframe.drop(columns=["index", "Index"])
    return dataframe
