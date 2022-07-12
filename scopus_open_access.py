from scopus_harvester.response_to_json import response_to_json
from scopus_harvester.file_to_data import file_to_data

def open_access(response):
    """Returns an indicator
    0 (is not open access),
    1 (is open access) or
    None (no open acces info).
    """
    output=[]
    f=response_to_json(response)
    data=file_to_data(f)
    if len(data)>0:
        for _ in range(len(data)):
            if data[_]["openaccess"] is None:
                output.append(None)
            else:
                output.append(data[_]["openaccess"])
    else:
        output.append(data[0]["openaccess"])
    return output


