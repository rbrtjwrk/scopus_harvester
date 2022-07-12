import pandas as pd

from scopus_harvester.scopus_get_journals import scopus_get_journals
from scopus_harvester.response_to_json import response_to_json
from scopus_harvester.file_to_data import file_to_data
from scopus_harvester.scopus_journal_title import scopus_journal_title
from scopus_harvester.scopus_journal_id import scopus_journal_id
from scopus_harvester.scopus_sjr import scopus_sjr
from scopus_harvester.scopus_citescore import scopus_citescore
from scopus_harvester.scopus_issn import parse_scopus_issn_dict, scopus_issn, scopus_eissn
from scopus_harvester.scopus_subject_area import scopus_subject_area
from scopus_harvester.scopus_subject_area_code import scopus_subject_area_code
from scopus_harvester.scopus_subject_classification import scopus_subject_classification
from scopus_harvester.scopus_open_access import scopus_open_access

def scopus_journals(subject_abbrev=None, count=None, start=0):
    """Retrieves journals from the Scopus Serial Title Metadata API.
    You can specify subject area abbreviation, count and start index for the retrieval,
    or you cal leave arguments empty - only count cannot be lower than 1.
    Returns a dataframe containing following columns: Journal Title, Journal ID, ISSN,
    eISSN, SJR, CiteScore, Subject_Area, Subject_Area_Code and Subject_Classification.
    """
    if count == None or count < 1:
        raise Exception("'count' cannot be lower than 1.")
    output=pd.DataFrame()
    response=scopus_get_journals(subject_abbrev=subject_abbrev, count=count, start=start)
    output["Journal_Title"]=scopus_journal_title(response)
    output["Journal_ID"]=scopus_journal_id(response)
    output["ISSN"]=scopus_issn(response)
    output["eISSN"]=scopus_eissn(response)
    output["SJR"]=scopus_sjr(response)
    output["CiteScore"]=scopus_citescore(response)
    output["Subject_Area"]=scopus_subject_area(response)
    output["Subject_Area_Code"]=scopus_subject_area_code(response)
    output["Subject_Classification"]=scopus_subject_classification(response)
    output["Open_Access"]=scopus_open_access(response)
    return output


