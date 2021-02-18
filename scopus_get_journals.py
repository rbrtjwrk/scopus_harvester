import json
import requests

def scopus_get_journals(subject_abbrev=None, count=None):
    payload={
            "Accept": "application/json",
            "X-ELS-APIKey": "e5011a9e1eb81eeea51a2abc18793df0"}
    parameters={
                "subj": subject_abbrev,
                "content": "journal",
                "count": count}
    response=requests.get("https://api.elsevier.com/content/serial/title", headers=payload, params=parameters)
    return response
