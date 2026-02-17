# Search Engine (CS 121)
Search engine with parsing and tokenization of HTML data from UCI subdomains.

Python packages required (`pip install`):
- `nltk`
- `beautifulsoup4`
- `lxml`
- `flask`

Required files/folders:
- `DEV` (in root directory)

Run indexer (no need if index already exists; this may take several hours to a day depending on computer speed; outputs `index_data` folder with partial indexes that are merged at the end):

`python indexer.py`

Run search engine (command line; may take about 3-10 minutes to start):

`python search_engine.py`

Run search engine (web; may take about 3-10 minutes to start):

`python search_engine.py web`