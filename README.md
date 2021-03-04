# scopus_harvester

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

```
df=scopus_journals("ARTS", 3)

df
                           Journal_Title   Journal_ID       ISSN  ...        Subject_Area   Subject_Area_Code                             Subject_Classification
0                     21st Century Music  18500162600  1534-3219  ...              [ARTS]              [1210]                                            [Music]
1  3L: Language, Linguistics, Literature  19700200922  0128-5157  ...  [ARTS, SOCI, ARTS]  [1203, 3310, 1208]  [Language and Linguistics, Linguistics and Lan...
2                                   452F  21101005201             ...              [ARTS]              [1208]                   [Literature and Literary Theory]

```

But first you have to set your API credentials in function _scopus_get_journals()_.

It is also possible to calculate SJR rank per subject area code per each serial title. To do that, run three following functions in the same order:

df=_multiply_journals(dataframe)_\
df=_rearrange_subject_attributes(dataframe)_\
df=_sjr_rank_per_subject_area_code(dataframe)_
