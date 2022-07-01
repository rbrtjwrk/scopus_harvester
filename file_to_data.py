
def file_to_data(file):
    """Retrieves entry’s data from
    the Scopus Serial Title Metadata API’s response.
    """
    return file["serial-metadata-response"]["entry"]


