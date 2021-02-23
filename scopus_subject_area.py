from scopus_harvester.response_to_json import response_to_json
from scopus_harvester.file_to_data import file_to_data

def scopus_subject_area(response):
    output=[]
    f=response_to_json(response)
    data=file_to_data(f)
    for _ in range(len(data)):
        if "subject-area" not in data[_].keys():
            output.append(" ")
        elif len(data[_]["subject-area"]) > 0:
            subject_areas=data[_]["subject-area"]
            subject_areas_abbrevs= [subject_areas[_]["@abbrev"] for _ in range(len(subject_areas))]
            output.append(subject_areas_abbrevs)
        else:
            output.append(data[_]["subject-area"]["@abbrev"])
    return output
