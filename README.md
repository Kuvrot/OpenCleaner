# OpenCleaner
Open-source cleaner program that removes all the cache files in the system. 

## How it works
* It cleans all the Cache in your system, by deleting all the directories that are named "cache" or that include the word "cache" in their name.
* Files that are protected or that are beign currently used will not be deleted.
* It only works on Windows for now.

## Run (pull requests are welcome!)
- Install customtkinter
  ```
  pip install customtkinter
  ```
- If using GIT, clone the repo with
  ```
  git clone https://github.com/Kuvrot/OpenCleaner.git
  ```
- Initialize the program with
  ```
  python main.py
  ````

![imagen](https://github.com/Kuvrot/OpenCleaner/assets/23508114/2fd94a97-cd83-4e9f-b15e-56abfa48277e)

## Known problems:
- If you have Unreal Engine installed and try to open a project you may encounter the following error:
 ```
  This project requires the 'Alembic Importer' plugin, which has a missing dependency on the 'Geometry Cache' plugin.
```
   * How to fix: Verify your Unreal engines installation. Note: Unreal engine projects may took longer to open for the first time after cleaning
- All your software may take longer to open the first time after cleaning.


