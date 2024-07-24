# Web Crawling with Scrapy

This project is designed to crawl websites and extract URLs efficiently. It crawls the entire website using Scrapy and stores the URLs in a file named `urls.json` inside a directory named after the project.in the same manner.

## Project Structure

The project creates a directory named after the project and stores the URLs in a file named `urls.json`.

## Features

- Crawls the entire website using Scrapy.
- Stores the extracted URLs in a JSON file.

## Requirements

- Python 3.x
- Scrapy

## Installation

1. **Clone the Repository**

   Clone the repository to your local machine.

   ```bash
   git clone https://github.com/kevit-naitri-doshi/Web-Crawling-with-Scrapy.git
   ```

2. **Install the Required Packages**

   Install the required Python packages using pip.

   ```bash
   pip install scrapy
   ```

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
   scrapy runspider spider.py -o project_name/urls.json
   ```

## Code Overview


### spider.py

This file contains the Scrapy spider for crawling the entire website when no sitemap is found. It extracts URLs and saves them in `urls.json`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
