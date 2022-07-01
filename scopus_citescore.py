from scopus_harvester.response_to_json import response_to_json
from scopus_harvester.file_to_data import file_to_data

def scopus_citescore(response):
    """Retrieves journal’s Citescore
    from the API’s response.
    """
    output=[]
    f=response_to_json(response)
    data=file_to_data(f)
    for _ in range(len(data)):
        if "citeScoreYearInfoList" in data[_]:
            output.append(data[_]["citeScoreYearInfoList"]["citeScoreCurrentMetric"])
        else:
            output.append(0.0)
    return output


