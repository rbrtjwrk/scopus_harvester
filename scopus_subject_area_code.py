def scopus_subject_area_code(response):
    output=[]
    f=response_to_json(response)
    data=file_to_data(f)
    for _ in range(len(data)):
        if len(data[_]["subject-area"]) > 0:
            subject_areas=data[_]["subject-area"]
            subject_areas_codes= [subject_areas[_]["@code"] for _ in range(len(subject_areas))]
            output.append(subject_areas_codes)
        else:
            output.append(data[_]["subject-area"]["@code"])
    return output
