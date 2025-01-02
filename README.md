# WikiHop: Recursive Wikipedia Article Navigator

WikiHop is a Python-based script that allows you to navigate Wikipedia articles recursively. Starting from a user-defined URL, the script follows random links within each article for a specified number of "hops," printing the title of each article it visits.

## Features

- **User-Controlled Navigation**: Specify the starting Wikipedia article and the number of hops to navigate.
- **Randomized Path**: Randomly selects a valid Wikipedia link to follow in each article.
- **Error Handling**: Includes robust error handling for network issues and unexpected HTML structures.
- **Responsible Scraping**:
  - Identifies itself using a `User-Agent` header.
  - Includes delays between requests to avoid overwhelming Wikipedia servers.

![image](https://github.com/user-attachments/assets/61228116-6bab-4fd2-9f3c-b7a148946178)


## Requirements

- Python 3.6 or higher
- The following Python packages:
  - `requests`
  - `beautifulsoup4`

You can install the required packages using:
```bash
pip install requests beautifulsoup4
