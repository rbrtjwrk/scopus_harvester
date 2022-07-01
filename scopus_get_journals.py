import json
import requests

def scopus_get_journals(subject_abbrev=None, count=None, start=0):
    """Retrieves journals from the Scopus Serial Title Metadata API.
    You can specify subject area abbreviation, count and start index for the retrieval,
    or you cal leave arguments empty - only count cannot be lower than 1.
    You have to specify X-ELS-APIKey within the function with your own API key.
    """
    payload={
            "Accept": "application/json",
            "X-ELS-APIKey": "YOUR_API_KEY"}
    parameters={
                "subj": subject_abbrev,
                "content": "journal",
                "count": count,
                "start": start}
    response=requests.get("https://api.elsevier.com/content/serial/title", headers=payload, params=parameters)
    return response


