import pandas as pd
import numpy as np

from scopus_harvester.multiply_journals import multiply_journals
from scopus_harvester.rearrange_subject_attributes import rearrange_subject_attributes

def sjr_rank_per_subject_area_code(dataframe):
    """Computes rank per subject area (code) based on SJR
    for all journals in a given dataframe.
    """
    dataframe=dataframe.copy()
    dataframe=multiply_journals(dataframe)
    dataframe=rearrange_subject_attributes(dataframe)
    if dataframe["SJR"][0] is not float:
        dataframe["SJR"]=[float(_) for _ in dataframe["SJR"]]
    dataframe["SJR"]=dataframe["SJR"].replace(0., np.nan)
    if dataframe["Subject_Area_Code"][0] is not str:
        dataframe["Subject_Area_Code"]=[" ".join(_) for _ in dataframe["Subject_Area_Code"]]
    dataframe["SJR_Rank_per_Subject_Area_Code"]=dataframe.groupby("Subject_Area_Code")["SJR"].rank(ascending=False)
    return dataframe


