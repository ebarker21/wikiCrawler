# wikiCrawler

A Python script that randomly traverses Wikipedia by following links from page to page, printing each article it visits along the way.

---

## Overview

`wikiCrawler` starts at a given Wikipedia article and continuously crawls to a randomly chosen linked article on each page, avoiding pages it has already visited. It uses `requests` to fetch pages and `lxml` to parse the HTML and extract links and titles.

**Tech Stack:**
- **Python** (100%)
- [`requests`](https://docs.python-requests.org/) — HTTP page fetching
- [`lxml`](https://lxml.de/) — HTML parsing and XPath link extraction
- [`uv`](https://github.com/astral-sh/uv) — dependency and environment management

**Project Structure:**
```
wikiCrawler/
├── pytravel.py       # Main crawler script
├── pyproject.toml    # Project metadata and dependencies
├── uv.lock           # Locked dependency versions
└── .python-version   # Pinned Python version
```

---

## Setup

### Prerequisites

- **Python 3.x** — check your version with `python --version`
- **[uv](https://github.com/astral-sh/uv)** — install with:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ebarker21/wikiCrawler.git
   cd wikiCrawler
   ```

2. **Install dependencies with uv:**
   ```bash
   uv sync
   ```

---

## Usage

Run the crawler with:

```bash
uv run pytravel.py
```

Or, if you prefer running it directly with Python after installing dependencies:

```bash
pip install requests lxml
python pytravel.py
```

The script starts at the **Linux** Wikipedia article by default and randomly hops between linked pages, printing the title of each page it visits:

```
Currently at Linux
Currently at GNU General Public License
Currently at Free Software Foundation
...
```

It will run indefinitely until it reaches a dead end (a page with no new unvisited Wikipedia links), at which point it prints:

```
Reached a dead end..?
```

### Changing the Start Page

To start from a different Wikipedia article, edit the `currentURL` variable near the bottom of `pytravel.py`:

```python
currentURL = 'https://en.wikipedia.org/wiki/YOUR_ARTICLE_HERE'
```

Replace `YOUR_ARTICLE_HERE` with the title of any Wikipedia article (e.g., `Python_(programming_language)`, `Black_hole`, `Atlanta`).
