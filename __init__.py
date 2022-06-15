import requests
import json
import pandas as pd
import numpy as np
import pkg_resources

from .scopus_get_journals import scopus_get_journals
from .response_to_json import response_to_json
from .file_to_data import file_to_data
from .scopus_journal_title import scopus_journal_title
from .scopus_journal_id import scopus_journal_id
from .scopus_sjr import scopus_sjr
from .scopus_citescore import scopus_citescore
from .scopus_issn import parse_scopus_issn_dict, scopus_issn, scopus_eissn
from .scopus_subject_areas import scopus_subject_areas
from .scopus_subject_area import scopus_subject_area
from .scopus_subject_area_code import scopus_subject_area_code
from .scopus_subject_classification import scopus_subject_classification
from .scopus_journals import scopus_journals
from .multiply_journals import multiply_journals
from .rearrange_subject_attributes import rearrange_subject_attributes
from .sjr_rank_per_subject_area_code import sjr_rank_per_subject_area_code
