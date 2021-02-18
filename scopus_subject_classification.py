from scopus_harvesting.reponse_to_json import response_to_json
from scopus_harvesting.file_to_data import file_to_data

def scopus_subject_classification(response):
    output=[]
    f=response_to_json(response)
    data=file_to_data(f)
    for _ in range(len(data)):
        if len(data[_]["subject-area"]) > 0:
            subject_areas=data[_]["subject-area"]
            subject_areas_abbrevs= [subject_areas[_]["$"] for _ in range(len(subject_areas))]
            output.append(subject_areas_abbrevs)
        else:
            output.append(data[_]["subject-area"]["$"])
    return output
