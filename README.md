# Search Engine (CS 121)
Search engine with parsing and tokenization of HTML data from UCI subdomains.

Python packages required (`pip install`):
- `nltk` (text processing)
- `beautifulsoup4` (parsing HTML)
- `lxml` (parsing XML/HTML)
- `flask` (web GUI)

Required files/folders:
- `DEV` (in root directory) (the "DEV_Test" folder is recommended for testing small amounts of data)

Run indexer (no need if index already exists; this may take several hours to a day depending on computer speed; outputs `index_data` folder with partial indexes that are merged at the end):

`python indexer.py`

Run search engine (command line; may take about 3-5 minutes to start):

`python search_engine.py`

Run search engine (web; may take about 3-5 minutes to start):

`python web_gui.py`

Compute analytics without rebuilding the entire index (2-3 minutes to finish):

`python analytics_compute.py`