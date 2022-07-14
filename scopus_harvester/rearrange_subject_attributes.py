import pandas as pd

def rearrange_subject_attributes(dataframe):
    """If a journal has more subject areas and codes,
    rearranges these so there is exactly
    one subject area/subject area code per row.
    Is executed as a part of processing
    of SJR rak per subject area (code).
    """
    output=dataframe.copy()
    jid_col_idx=output.columns.get_loc("Journal_ID")
    sc_col_idx=output.columns.get_loc("Subject_Classification")
    sac_col_idx=output.columns.get_loc("Subject_Area_Code")
    sa_col_idx=output.columns.get_loc("Subject_Area")
    for i, row in enumerate(output.itertuples(), 0):
        #rearrange subject area
        if len(row.Subject_Area) > 1:
            border_1=sum(output.iloc[:i, jid_col_idx]==row.Journal_ID)
            border_2=sum(output.iloc[i:, jid_col_idx]==row.Journal_ID)-1
            output.iloc[i, sa_col_idx]=row.Subject_Area[border_1:(len(row.Subject_Area)-border_2)]
        #rearrange subject area code
        if len(row.Subject_Area_Code) > 1:
            border_1=sum(output.iloc[:i, jid_col_idx]==row.Journal_ID)
            border_2=sum(output.iloc[i:, jid_col_idx]==row.Journal_ID)-1
            output.iloc[i, sac_col_idx]=row.Subject_Area_Code[border_1:(len(row.Subject_Area_Code)-border_2)]
        #rearrange subject classification
        if len(row.Subject_Classification) > 1:
            border_1=sum(output.iloc[:i, jid_col_idx]==row.Journal_ID)
            border_2=sum(output.iloc[i:, jid_col_idx]==row.Journal_ID)-1
            output.iloc[i, sc_col_idx]=row.Subject_Classification[border_1:(len(row.Subject_Classification)-border_2)]
    output.Subject_Classification=[_[0] if type(_)==list else _ for _ in output.Subject_Classification]
    output.Subject_Area_Code=[int(_[0]) if type(_)==list else int(_) for _ in output.Subject_Area_Code]
    output.Subject_Area=[_[0] if type(_)==list else _ for _ in output.Subject_Area]
    return output


