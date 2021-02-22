# scopus_harvesting

Set of functions to call _Scopus Serial Title Metadata API_ and harvest following serial title's attributes:

| Scopus Serial Title's attributes |
| -------------------------------- |
| Journal Title                    |
| Journal ID                       |
| SJR                              |
| Citescore                        |
| ISSN                             |
| Scopus Subject Area              |
| Scopus Subject Area Code         |
| Scopus Subject Classification    |

Although it is possible to call standalone functions separately, I recommend you to call function _scopus_journals(subject_abbrev, count)_ to obtain all of the attributes at once. List of all subject areas can be found at https://dev.elsevier.com/.

But first you have to set your API credentials in function _scopus_get_journals(subject, count)_.

It is also possible to calculate SJR rank per subject area code per each serial title. To do that, run two following functions:

df=_multiply_journals(dataframe)_\
df=_sjr_rank_per_subject_area_code(dataframe)_
