from scopus_harvester.response_to_json import response_to_json
from scopus_harvester.file_to_data import file_to_data

def scopus_sjr(response):
    """Retrieves journal’s SJR
    from the API’s response.
    """
    output=[]
    f=response_to_json(response)
    data=file_to_data(f)
    for _ in range(len(data)):
        if "SJRList" in data[_]:
            output.append(list(data[_]["SJRList"]["SJR"][0].values())[2])
        else:
            output.append(0.0)
    return output


