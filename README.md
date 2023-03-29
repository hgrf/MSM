# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/hgrf/racine/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                                                               |    Stmts |     Miss |   Cover |   Missing |
|----------------------------------------------------------------------------------- | -------: | -------: | ------: | --------: |
| app/\_\_init\_\_.py                                                                |       65 |        4 |     94% |     84-88 |
| app/api/\_\_init\_\_.py                                                            |        3 |        0 |    100% |           |
| app/api/actions.py                                                                 |       99 |       57 |     42% |72-101, 122-129, 152-158, 181-212, 235-258 |
| app/api/common.py                                                                  |        5 |        0 |    100% |           |
| app/api/errors.py                                                                  |       11 |        7 |     36% |  6-11, 15 |
| app/api/fields.py                                                                  |       82 |       55 |     33% |20-25, 29-34, 111-133, 159-218 |
| app/api/samples.py                                                                 |      104 |       67 |     36% |57-79, 100-107, 128-133, 154-159, 182-229 |
| app/api/shares.py                                                                  |       63 |       43 |     32% |49-75, 101-126 |
| app/auth/\_\_init\_\_.py                                                           |        3 |        0 |    100% |           |
| app/auth/forms.py                                                                  |       15 |        0 |    100% |           |
| app/auth/views.py                                                                  |       75 |       37 |     51% |18-21, 34, 40-42, 51, 72-94, 99-109, 116-120 |
| app/browser/\_\_init\_\_.py                                                        |        3 |        0 |    100% |           |
| app/browser/views.py                                                               |      300 |      247 |     18% |58-78, 99-125, 129-142, 146-162, 184-240, 260, 284-331, 349-374, 391-418, 426-486, 495-520, 528-569, 577-584, 591-626, 630-634 |
| app/config.py                                                                      |       31 |        0 |    100% |           |
| app/decorators.py                                                                  |       12 |        3 |     75% |     10-12 |
| app/emailing.py                                                                    |       17 |       11 |     35% |9-19, 26-29 |
| app/main/\_\_init\_\_.py                                                           |        3 |        0 |    100% |           |
| app/main/errors.py                                                                 |       19 |        6 |     68% |9, 19, 24-28 |
| app/main/forms.py                                                                  |       21 |        3 |     86% |     26-28 |
| app/main/views.py                                                                  |      164 |      121 |     26% |26-42, 56-141, 160-173, 185-217, 231-232, 238-279, 292-343, 349-358, 368 |
| app/models.py                                                                      |      300 |      130 |     57% |24, 29, 33-83, 87-112, 124-125, 128-129, 158, 162, 166, 172-173, 177-187, 194, 203-209, 212, 216-219, 256-274, 277, 290-308, 314, 326-340, 359, 362-368, 371, 397-422, 426-434, 459, 470, 483, 496, 512, 519, 529 |
| app/printdata/\_\_init\_\_.py                                                      |        3 |        0 |    100% |           |
| app/printdata/forms.py                                                             |        8 |        0 |    100% |           |
| app/printdata/views.py                                                             |       43 |       34 |     21% |     12-52 |
| app/profile/\_\_init\_\_.py                                                        |        3 |        0 |    100% |           |
| app/profile/forms.py                                                               |       24 |        6 |     75% |37-38, 41-45, 48-49 |
| app/profile/views.py                                                               |       55 |       40 |     27% |12-23, 29-38, 44-70 |
| app/settings/\_\_init\_\_.py                                                       |        3 |        0 |    100% |           |
| app/settings/forms.py                                                              |       29 |        0 |    100% |           |
| app/settings/views.py                                                              |      176 |      132 |     25% |21, 28-54, 66-82, 91-140, 147-179, 190-198, 202-215, 224-274, 287-290 |
| app/smbinterface.py                                                                |       83 |       67 |     19% |29-51, 57-71, 92-107, 111-143, 147, 152-169 |
| app/tests/\_\_init\_\_.py                                                          |        0 |        0 |    100% |           |
| app/tests/test\_main.py                                                            |       32 |        0 |    100% |           |
| app/usagestats.py                                                                  |       55 |       31 |     44% |21-22, 35, 39-85, 89-99 |
| app/validators.py                                                                  |       14 |        9 |     36% |6-7, 11-12, 16-21 |
| migrations/env.py                                                                  |       33 |       10 |     70% |43-47, 62-66, 88 |
| migrations/versions/1de13fd625b1\_added\_archived\_flag.py                         |        9 |        1 |     89% |        26 |
| migrations/versions/2fcf420c6c0c\_added\_path\_column\_to\_smbres.py               |        8 |        1 |     88% |        25 |
| migrations/versions/3d9e4225ecbd\_remove\_unique\_constraint\_from\_sample\_.py    |       12 |        1 |     92% |        50 |
| migrations/versions/4ca6d5b7b966\_initial\_migration.py                            |       28 |       10 |     64% |   126-135 |
| migrations/versions/5ae6e19e0a7b\_added\_column\_for\_inheriting\_data.py          |       12 |        3 |     75% |     27-29 |
| migrations/versions/9c070b1a9f8b\_add\_news.py                                     |       15 |        3 |     80% |     86-88 |
| migrations/versions/17c32bd785e3\_added\_size\_column\_to\_uploads\_table.py       |        8 |        1 |     88% |        25 |
| migrations/versions/31fd4405fcd2\_removed\_unused\_columns\_and\_tables.py         |       16 |        1 |     94% |        75 |
| migrations/versions/50d1a487c7ab\_added\_ordnum\_and\_datecreated\_to\_action\_.py |       12 |        2 |     83% |     28-29 |
| migrations/versions/70dd6f0306c4\_added\_last\_modified\_field\_to\_sample\_.py    |        8 |        1 |     88% |        25 |
| migrations/versions/71c1f7625171\_add\_user\_tokens.py                             |       12 |        3 |     75% |     27-29 |
| migrations/versions/86ec305ceaa7\_add\_collaborative\_sample\_flag.py              |        9 |        1 |     89% |        26 |
| migrations/versions/365a26270961\_added\_extension\_column\_to\_uploads\_table.py  |        8 |        1 |     88% |        25 |
| migrations/versions/506bb8a29f4d\_add\_mountpoint\_column.py                       |       12 |        1 |     92% |        40 |
| migrations/versions/3180b28651e3\_added\_isdeleted\_flag\_to\_sample.py            |        8 |        1 |     88% |        25 |
| migrations/versions/362505d00f1a\_repair\_broken\_heir\_column.py                  |       15 |        1 |     93% |        47 |
| migrations/versions/449283d5217f\_added\_sample\_description\_column.py            |        8 |        1 |     88% |        25 |
| migrations/versions/591022583d54\_added\_hash\_column\_to\_uploads\_table.py       |        8 |        1 |     88% |        25 |
| migrations/versions/578518528886\_added\_ownership\_to\_actions.py                 |       13 |        3 |     77% |     28-30 |
| migrations/versions/a45942d815f\_added\_upload\_table.py                           |        8 |        1 |     88% |        35 |
| migrations/versions/cb354c75d49\_added\_activity\_table.py                         |       10 |        2 |     80% |     52-53 |
|                                                                          **TOTAL** | **2195** | **1160** | **47%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/hgrf/racine/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/hgrf/racine/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/hgrf/racine/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/hgrf/racine/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2Fhgrf%2Fracine%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/hgrf/racine/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.