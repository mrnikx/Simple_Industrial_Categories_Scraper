# Simple Industrial Categories Scraper

This project is a simple web scraper that extracts industrial categories from a specified Wikipedia page using Python. The scraped data is saved in an Excel file for further analysis or reference.

## Features

- Scrapes industrial categories and their respective industries from a Wikipedia page.
- Excludes irrelevant categories based on predefined filters.
- Saves the extracted data in an Excel file.

## Requirements

To run this project, you will need:

- Python 3.x
- The following Python libraries:
  - requests
  - beautifulsoup4
  - pandas
  - openpyxl (for saving to Excel)

You can install the required libraries using pip:

bash
`pip install requests beautifulsoup4 pandas openpyxl`


## Usage

1. Clone the repository or download the script.
2. Open the script file and set the URL variable to the desired Wikipedia page containing industrial categories.
3. Run the script:

    bash
`python scraper.py`


4. After execution, an Excel file named tabriz_industries.xlsx will be created in the same directory, containing the extracted data.

## Configuration

You can customize the list of excluded categories by modifying the excluded_categories variable in the script. This allows you to filter out any categories you do not wish to include in the output.

## Logging

The script uses Python's built-in logging module to provide information about its execution process. You can see warnings and errors in the console while the script is running.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Wikipedia](https://www.wikipedia.org/) for providing the data.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) for parsing HTML and XML documents.
- [Pandas](https://pandas.pydata.org/) for data manipulation and analysis.

## Author

Mahdi Ahmadi Nik

mahdi.itx@gmail.com