# Clutch.co-webscraper

### Automatically web scrapes this website [clutch.co](https://clutch.co) to get the following details
1. Company name
2. Website Link
3. Rating count
4. Minimum project size
5. Hourly rate
6. Number of employees
7. Location

### Exports as xlsx
Packs this data as python dictionary to create a pandas dataframe.  
This dataframe is then written to xlsx workbook according to the domain of the company like web development, UI/UX as a separate sheet in the same xlsx workbook.

### Using the script
`python scraper.py`

### Input
`Enter max page limit : 5`<br>
`Enter max domains limit : 5`<br>

*Max domain limit defines the max no of domains to be queried.<br>
Max page limit defines the max no of pages to be scraped for a particular domain.*
