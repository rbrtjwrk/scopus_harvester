from scopus_harvesting.scopus_get_journals import scopus_get_journals
from scopus_harvesting.response_to_json import response_to_json
from scopus_harvesting.file_to_data import file_to_data
from scopus_harvesting.scopus_journal_title import scopus_journal_title
from scopus_harvesting.scopus_journal_id import scopus_journal_id
from scopus_harvesting.scopus_sjr import scopus_sjr
from scopus_harvesting.scopus_citescore import scopus_citescore
from scopus_harvesting.scopus_iss import parse_scopus_issn_dict, scopus_issn
from scopus_harvesting.scopus_subject_area import scopus_subject_area
from scopus_harvesting.scopus_subject_area_code import scopus_subject_area_code
from scopus_harvesting.scopus_subject_classification import 

def scopus_journals(subject=None, count=None):
    output=pd.DataFrame()
    response=scopus_get_journals(subject=subject, count=count)
    output["Journal_Title"]=scopus_journal_title(response)
    output["Journal_ID"]=scopus_journal_id(response)
    output["ISSN"]=scopus_issn(response)
    output["SJR"]=scopus_sjr(response)
    output["CiteScore"]=scopus_citescore(response)
    output["Subject_Area"]=scopus_subject_area(response)
    output["Subject_Area_Code"]=scopus_subject_area_code(response)
    output["Subject_Classification"]=scopus_subject_classification(response)
    return output
