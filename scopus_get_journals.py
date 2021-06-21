import json
import requests

def scopus_get_journals(subject_abbrev=None, count=None, start=0):
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
