def scopus_sjr(response):
    output=[]
    f=response_to_json(response)
    data=file_to_data(f)
    for _ in range(len(data)):
        if "SJRList" in data[_]:
            output.append(list(data[_]["SJRList"]["SJR"][0].values())[2])
        else:
            output.append(0.0)
    return output
