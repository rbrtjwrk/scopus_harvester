# scopus_harvesting

Set of functions to call _Scopus Serial Title Metadata API_ and harvest following Journal's attributes:

| Scopus Journal's attributes   |
| ----------------------------- |
| Journal Title                 |
| Journal ID                    |
| SJR                           |
| Citescore                     |
| ISSN                          |
| Scopus Subject Area           |
| Scopus Subject Area Code      |
| Scopus Subject Classification |

Call function _scopus_journals(subject_abbrev, count)_ to obtain all of the attributes at once. List of all subject areas can be found at https://dev.elsevier.com/.

But first you have to set your API credentials in function _scopus_get_journals_.
