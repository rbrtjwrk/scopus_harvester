def parse_scopus_issn_dict(issn_dict):
    issns=[list(issn_dict[_].values()) for _ in range(len(issn_dict))]
    issns=[issn for list in issns for issn in list]
    return issns

def scopus_issn(response):
    output=[]
    f=response_to_json(response)
    data=file_to_data(f)
    if len(data)>0:
        for _ in range(len(data)):
            if "prism:issn" in data[_]:
                if isinstance(data[_]["prism:issn"], str):
                    output.append(data[_]["prism:issn"])
                else:
                    output.append(parse_scopus_issn_dict(data[_]["prism:issn"]))
            else:
                output.append(" ")
    else:
        output=data[0]["prism:issn"]
    return output
