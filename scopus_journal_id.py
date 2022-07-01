from scopus_harvester.response_to_json import response_to_json
from scopus_harvester.file_to_data import file_to_data

def scopus_journal_id(response):
    """Retrieves journal’s id
    from the API’s response.
    """
    f=response_to_json(response)
    data=file_to_data(f)
    output=[data[_]["source-id"] for _ in range(len(data))]
    return output


