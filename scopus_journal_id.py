def scopus_journal_id(response):
    f=response_to_json(response)
    data=file_to_data(f)
    output=[data[_]["source-id"] for _ in range(len(data))]
    return output
