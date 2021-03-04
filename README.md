# scopus_harvester

A set of functions to call **_Scopus Serial Title Metadata API_** and harvest following serial title's attributes:

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

Although it is possible to call standalone functions separately, I recommend you to call function _scopus_journals(subject_abbrev, count)_ to obtain all of the attributes at once.

To see all Scopus Subject Areas, call function _scopus_subject_areas()_.

```
>>> import scopus_harvester as sh
>>> 
>>> sh.scopus_subject_areas().head()
>>> 
>>>   Subject_Area                        Subject_Area: Full_Name
0         AGRI               Agricultural and Biological Sciences
1         ARTS                                Arts and Humanities
2         BIOC       Biochemistry, Genetics and Molecular Biology
3         BUSI                Business, Management and Accounting
4         CENG                               Chemical Engineering
>>>
>>> df=sh.scopus_journals("ARTS", 3)
>>>
>>> df
                           Journal_Title   Journal_ID       ISSN  ...        Subject_Area   Subject_Area_Code                             Subject_Classification
0                     21st Century Music  18500162600  1534-3219  ...              [ARTS]              [1210]                                            [Music]
1  3L: Language, Linguistics, Literature  19700200922  0128-5157  ...  [ARTS, SOCI, ARTS]  [1203, 3310, 1208]  [Language and Linguistics, Linguistics and Lan...
2                                   452F  21101005201             ...              [ARTS]              [1208]                   [Literature and Literary Theory]
[3 rows x 8 columns]
>>>

```

But first you have to set your API credentials in function _scopus_get_journals()_.

It is also possible to calculate SJR rank per subject area code per each serial title. To do that, run three following functions in the same order:

```
>>> df=sh.multiply_journals(df)
>>> df=sh.rearrange_subject_attributes(df)
>>> df=sh.sjr_rank_per_subject_area_code(df)
>>>
>>> df.iloc[:, [0,6,8]]
                           Journal_Title Subject_Area_Code  SJR_Rank_per_Subject_Area_Code
0                     21st Century Music              1210                             1.0
1  3L: Language, Linguistics, Literature              1203                             1.0
2  3L: Language, Linguistics, Literature              3310                             1.0
3  3L: Language, Linguistics, Literature              1208                             1.0
4                                   452F              1208                             NaN
>>>
```

**Note that the SJR rank per subject area code is computed only on the data you harvest. Also, for journals that do not have a SJR, the rank is not computed.**
