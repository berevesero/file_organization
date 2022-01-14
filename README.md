# file_organization

In the present implementation, the script is primarily used to organize images and videos into directories (but it can of course be used for other files as well). However, the script assumes that the files have the following name format: Year-Month-Day...
So for example: 2022-01-01CoolPhoto.jpg, 2022-01-02_funny_video.mov, 2021-05-16_GoodTime.mp3

The following directories structure is created, based on year and month, and the files are moved into it accordingly:
```
BASE/DIRECTORY
|-- 2021
| |-- 05
| | |-- 2021-05-16_GoodTime.mp3
|-- 2022
| |-- 01
| | |-- 2022-01-01CoolPhoto.jpg
| | |-- 2022-01-02_funny_video.mov
```

The BASE/DIRECTORY can be set with the variable `DIRECTORY`
