import pandas as pd

def rearrange_subject_attributes(dataframe):
    """If a journal has more subject areas and codes,
    rearranges these so there is exactly
    one subject area/subject area code per row.
    Is executed as a part of processing
    of SJR rak per subject area (code).
    """
    output=dataframe.copy()
    jt_col_idx=output.columns.get_loc("Journal_Title")
    sc_col_idx=output.columns.get_loc("Subject_Classification")
    sac_col_idx=output.columns.get_loc("Subject_Area_Code")
    sa_col_idx=output.columns.get_loc("Subject_Area")
    for i, row in enumerate(output.itertuples(), 0):
        #rearrange subject classification
        if len(row.Subject_Classification) > 1:
            border_1=sum(output.iloc[:i, jt_col_idx]==row.Journal_Title)
            border_2=sum(output.iloc[i:, jt_col_idx]==row.Journal_Title)-1
            output.iloc[i, sc_col_idx]=row.Subject_Classification[border_1:(len(row.Subject_Classification)-border_2)]
        #rearrange subject area code
        if len(row.Subject_Area_Code) > 1:
            border_1=sum(output.iloc[:i, jt_col_idx]==row.Journal_Title)
            border_2=sum(output.iloc[i:, jt_col_idx]==row.Journal_Title)-1
            output.iloc[i, sac_col_idx]=row.Subject_Area_Code[border_1:(len(row.Subject_Area_Code)-border_2)]
        #rearrange subject area
        if len(row.Subject_Area) > 1:
            border_1=sum(output.iloc[:i, jt_col_idx]==row.Journal_Title)
            border_2=sum(output.iloc[i:, jt_col_idx]==row.Journal_Title)-1
            output.iloc[i, sa_col_idx]=row.Subject_Area[border_1:(len(row.Subject_Area)-border_2)]
    return output


