# scopus_harvester

#### Requirements
json 2.0.9, Requests 2.25.1, Pandas, Numpy, pkg resources

## description

A set of functions to call **_Scopus Serial Title Metadata API_** and harvest following serial title's attributes:

| Scopus Serial Title's attributes |
| -------------------------------- |
| Journal Title                    |
| Journal ID                       |
| SJR                              |
| Citescore                        |
| ISSN                             |
| eISSN                            |
| Scopus Subject Area              |
| Scopus Subject Area Code         |
| Scopus Subject Classification    |
| Open Access                      |


Although it is possible to call standalone functions separately, I recommend you to call the function _scopus_journals(subject_abbrev=None, subject_code=None, count=None, start=0)_ to obtain all of the attributes at once.

To see all Scopus Subject Areas, call function _scopus_subject_areas()_.


```
>>> import scopus_harvester as sh
>>> 
>>> sh.scopus_subject_areas().head()
  Subject_Area                        Subject_Area: Full_Name
0         AGRI           Agricultural and Biological Sciences
1         ARTS                            Arts and Humanities
2         BIOC   Biochemistry, Genetics and Molecular Biology
3         BUSI            Business, Management and Accounting
4         CENG                           Chemical Engineering
>>>
```


Before harvesting, you must first manually set up your API Key in the file _scopus_get_journals.py_.

Then call the function _scopus_journals(subject_abbrev=None, count=None, start=0)_.<br/>
Parameters:<br/>
    ⋅⋅⋅ **subject_abbrev**: str, default _None_; you could either leave this parameter unspecified or select exactly one subject area.<br/>
    ⋅⋅⋅ **count**: int, default _None_; count cannot be lower than 1.<br/>
    ⋅⋅⋅ **start**: int, default 0.


```
>>> df=sh.scopus_journals(subject_abbrev="ARTS", count=3, start=0)
>>>
>>> df
                           Journal_Title   Journal_ID       ISSN  ...  Subject_Area_Code                                 Subject_Classification  Open_Access
0                     21st Century Music  18500162600  1534-3219  ...  [1210]              [Music]                                               None
1  3L: Language, Linguistics, Literature  19700200922  0128-5157  ...  [1203, 3310, 1208]  [Language and Linguistics, Linguistics and Language]  1
2                                   452F  21101005201             ...  [1208]              [Literature and Literary Theory]                      1
[3 rows x 8 columns]
>>>
```


If you want to harvest all Scopus sources at once, you may encounter API limits, therefore it is advisable to dowload the data in batches. E.g. harvest data in batches per subject area/subject code:

```
import pandas as pd
import scopus_harvester as sh

def get_entries(subject_area):
    output=[]
    s=0
    for _ in range(1000):
        try:
            r=sh.scopus_journals(subject_abbrev=subject_area, count=200, start=s)
            ooutput.append(r)
            s+=200
        # if there are no more journals in a given subject area
        except KeyError: 
            return output

def flatten_dfs(list_of_dfs):
    ooutput=pd.DataFrame()
    for _ in list_of_dfs:
        output=output.append(_)
    return output

>>> subject_areas=sh.scopus_subject_areas()

>>> res=pd.DataFrame()

>>> for sa in subject_areas.Subject_Area:
...    print(sa)
...    entries=get_entries(sa)
...    print("--- entries downloaded")
...    flattened_entries=flatten_dfs(entries)
...    print(f"--- {sa}: {len(flattened_entries)}")
...    print("--- entries flattend")
...    res=res.append(flattened_entries)
...    print("--- entries appended")
...    print("")

```


It is also possible to compute SJR rank per subject area code per each serial title. To do that, call the function _sjr_rank_per_subject_area_code(dataframe)_.


```
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
