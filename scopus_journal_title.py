def scopus_journal_title(response):
    f=response_to_json(response)
    data=file_to_data(f)
    output=[data[_]["dc:title"] for _ in range(len(data))]
    return output
