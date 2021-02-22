import pandas as pd

def multiply_journals(dataframe, alphabetical_order=True):
    for row in dataframe.itertuples():
        multiply_by=len(row.Subject_Classification)
        if multiply_by > 1:
            dataframe=dataframe.append([row] * (multiply_by-1), sort=False)
    dataframe=dataframe.drop(columns=["Index"])
    if alphabetical_order==True:
        dataframe=dataframe.sort_values(by="Journal_Title")
    return dataframe
