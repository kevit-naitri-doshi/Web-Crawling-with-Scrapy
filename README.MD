# Web Crawling with Scrapy

This project is designed to crawl websites and extract URLs efficiently. It first checks if a sitemap is available for the website. If a sitemap is found, it scrapes the sitemap using Selenium and stores the URLs in a file named `urls.json` inside a directory named after the project. If no sitemap is found, it crawls the entire website using Scrapy and stores the URLs in the same manner.

## Project Structure

The project creates a directory named after the project and stores the URLs in a file named `urls.json`.

## Features

- Checks for the presence of a sitemap on the website.
- If a sitemap is available, scrapes it using Selenium.
- If no sitemap is found, crawls the entire website using Scrapy.
- Stores the extracted URLs in a JSON file.

## Requirements

- Python 3.x
- Selenium
- Scrapy
- ChromeDriver (or another WebDriver for Selenium)

## Installation

1. **Clone the Repository**

   Clone the repository to your local machine.

   ```bash
   git clone https://github.com/kevit-naitri-doshi/Web-Crawling-with-Scrapy.git
   ```

2. **Install the Required Packages**

   Install the required Python packages using pip.

   ```bash
   pip install selenium scrapy
   ```

3. **Set Up ChromeDriver**

   Download and install ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your system's PATH.

## Configuration

You can change the crawler's parameters by modifying the `config.py` file. This file includes settings such as the project name and the starting URL.

### config.py

Set your desired parameters such as the project name and the starting URL.

## How to Use

1. **Configure the Parameters**

   Open `config.py` and set your desired parameters such as the project name and the starting URL.

2. **Run the Crawler**

   Run the Python script to start the crawling process.

   ```bash
   python main.py
   ```

## Code Overview

### check_sitemap.py

This file checks if a sitemap is present on the website and contains the logic for scraping the sitemap using Selenium.

### spider.py

This file contains the Scrapy spider for crawling the entire website when no sitemap is found. It extracts URLs and saves them in `urls.json`.

### main.py

This file contains the main script to start the crawling process. It checks for a sitemap and decides whether to use Selenium or Scrapy based on its presence.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
