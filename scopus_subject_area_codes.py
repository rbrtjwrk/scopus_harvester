import pandas as pd
import pkg_resources

def scopus_subject_area_codes():
    """Lists Scopus subject area codes
    and their subject classifications.
    """
    path=pkg_resources.resource_filename("scopus_harvester", "data/scopus_subject_area_codes.txt")
    output=pd.read_table(path, delimiter="-")
    return output
