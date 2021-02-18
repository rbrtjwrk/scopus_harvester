def scopus_journals(response):
    output=pd.DataFrame()
    output["Journal_Title"]=scopus_journal_title(response)
    output["Journal_ID"]=scopus_journal_id(response)
    output["ISSN"]=scopus_issn(response)
    output["SJR"]=scopus_sjr(response)
    output["CiteScore"]=scopus_citescore(response)
    output["Subject_Area"]=scopus_subject_area(response)
    output["Subject_Area_Code"]=scopus_subject_area_code(response)
    output["Subject_Classification"]=scopus_subject_classification(response)
    return output
