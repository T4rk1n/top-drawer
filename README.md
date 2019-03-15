# Top Drawer

Command line tool to search for synonyms and validate if they are available on pypi or npm.

### Install

Python >= 3.6:

`$ pip install top-drawer`

### Usage

```
$ top-drawer --help
top-drawer 0.0.1
usage: top-drawer [-h] [-v] {search,validate,clear-cache} ...

    Search for synonyms and validate if the name is available on pypi or npm.
    

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose

Commands:
  {search,validate,clear-cache}
    search              Search for valid synonyms of the provided word.
    validate            Validate a name is available
    clear-cache         Clear the validations cache.
```

