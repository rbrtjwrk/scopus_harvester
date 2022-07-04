import pandas as pd
import numpy as np

from scopus_harvester.multiply_journals import multiply_journals
from scopus_harvester.rearrange_subject_attributes import rearrange_subject_attributes

def sjr_rank_per_subject_area_code(dataframe):
    """Computes rank per subject area (code) based on SJR
    for all journals in a given dataframe.
    """
    output=dataframe.copy()
    output=multiply_journals(output)
    output=rearrange_subject_attributes(output)
    if output["SJR"][0] is not float:
        output["SJR"]=[float(_) for _ in output["SJR"]]
    output["SJR"]=output["SJR"].replace(0., np.nan)
    if output["Subject_Area_Code"][0] is not str:
        output["Subject_Area_Code"]=[" ".join(_) for _ in output["Subject_Area_Code"]]
    output["SJR_Rank_per_Subject_Area_Code"]=output.groupby("Subject_Area_Code")["SJR"].rank(ascending=False)
    return output


