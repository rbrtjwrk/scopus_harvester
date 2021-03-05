import pandas as pd
import pkg_resources

def scopus_subject_areas():
    path=pkg_resources.resource_filename("scopus_harvester", "data/scopus_subject_areas.txt")
    output=pd.read_table(path, delimiter="-")
    return output
