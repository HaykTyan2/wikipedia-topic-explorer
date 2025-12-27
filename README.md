# wikipedia-topic-explorer

A Python-based Wikipedia crawler that explores article links starting from a user-defined article, with configurable depth and page limits.

This project is intended as a learning tool for understanding web scraping, basic crawling logic, and Python project structure.

------------------------------------------------------------------------------------------------------------------------------

## What this project does

The program starts from a Wikipedia article chosen by the user and follows links to other Wikipedia articles.

The user can control:
- The starting article (URL or article name)
- How deep the crawler is allowed to go
- The maximum number of pages to visit
- Whether the discovered links should be saved to a CSV file

The crawler only follows valid Wikipedia article links and avoids special pages such as files, categories, and help pages.

------------------------------------------------------------------------------------------------------------------------------

## How it works (high level)

1. The user provides a starting article.
2. The crawler fetches the page HTML.
3. All valid Wikipedia article links are extracted.
4. The crawler continues following links until:
   - The maximum depth is reached, or
   - The maximum number of pages is reached.
5. The final list of visited URLs is printed.
6. Optionally, the results are saved to a CSV file.

------------------------------------------------------------------------------------------------------------------------------

## Project structure
```
wikipedia-topic-explorer/
├── src/
│ ├── explorer.py # Crawl logic and traversal control
│ ├── scraper.py # Handles HTTP requests to Wikipedia
│ ├── parser.py # Extracts valid links from HTML
│ ├── utils.py # Helper functions for filtering links
│
├── tests/
│ ├── test_scraper.py # Basic tests for scraping logic
│ └── __init__.py
│
├── main.py # Entry point and CLI interaction
├── requirements.txt # Project dependencies
├── randomWords.txt # Optional word list for generating CSV filenames
├── README.md
```
------------------------------------------------------------------------------------------------------------------------------

## File explanations

### `main.py`
This is the entry point of the program.

It is responsible for:
- Parsing command-line arguments
- Asking the user for input if arguments are not provided
- Normalizing the starting article into a valid Wikipedia URL
- Calling the crawler
- Printing results
- Saving results to a CSV file if requested

------------------------------------------------------------------------------------------------------------------------------

### `src/explorer.py`
Contains the main crawling logic.

This file:
- Tracks visited URLs
- Keeps track of crawl depth
- Limits the number of pages visited
- Coordinates fetching pages and extracting links

------------------------------------------------------------------------------------------------------------------------------

### `src/scraper.py`
Handles fetching HTML from Wikipedia.

This file:
- Uses the `requests` library
- Sends a proper User-Agent header
- Raises errors if a request fails

------------------------------------------------------------------------------------------------------------------------------

### `src/parser.py`
Extracts links from Wikipedia pages.

This file:
- Uses BeautifulSoup to parse HTML
- Finds all anchor (`<a>`) tags
- Filters links to include only valid Wikipedia article URLs

------------------------------------------------------------------------------------------------------------------------------

### `src/utils.py`
Contains helper functions.

Currently, this file:
- Filters out unwanted Wikipedia links such as:
  - Main page
  - File pages
  - Category pages
  - Help and special pages

---

### `randomWords.txt`
This file contains a list of words used only to generate a default CSV filename if the user chooses to save results but does not provide a filename.

This file is optional and not required for the crawler itself to function.

------------------------------------------------------------------------------------------------------------------------------

## Installation:
1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/wikipedia-topic-explorer.git
cd wikipedia-topic-explorer
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
## Usage
Run the program:
```
python main.py
```
------------------------------------------------------------------------------------------------------------------------------

## You will be prompted to:
• Enter a starting Wikipedia article (URL or name)
• Enter crawl depth
• Enter the maximum number of pages
• Choose whether to save results to a CSV file

## You can also run it with command-line arguments:
```
python main.py --start Albert_Einstein --depth 2 --pages 15 --save results.csv
```
------------------------------------------------------------------------------------------------------------------------------

## Output:
• All discovered article URLs are printed to the console.
• If CSV export is enabled, the results are saved to the data/ directory.
• The CSV file contains one URL per row.

------------------------------------------------------------------------------------------------------------------------------

## Notes and limitations:
• This crawler is intentionally simple and synchronous.
• It is not optimized for speed or large-scale crawling.
• It is designed for educational purposes.
• The crawler respects Wikipedia usage policies by limiting request volume.

------------------------------------------------------------------------------------------------------------------------------

## License:
This project is provided for educational use.
