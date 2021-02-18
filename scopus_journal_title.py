from scopus_harvesting.response_to_json import response_to_json
from scopus_harvesting.file_to_data import file_to_data

def scopus_journal_title(response):
    f=response_to_json(response)
    data=file_to_data(f)
    output=[data[_]["dc:title"] for _ in range(len(data))]
    return output
