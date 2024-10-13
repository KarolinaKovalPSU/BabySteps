# COVID-19 Data Scraper and Visualizer

A Python script that uses Selenium to scrape COVID-19 statistics from the CDC website and visualize the data trends using Matplotlib.

## Features

- Scrapes COVID-19 data from multiple CDC web pages.
- Extracts key statistics like test positivity, emergency department visits, hospitalizations, and deaths.
- Visualizes trends over time using line graphs.

## Requirements

- Python 3.x
- Selenium
- Pandas
- Matplotlib
- ChromeDriver (compatible with your version of Chrome)

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.x installed on your machine.
3. Install the required libraries:

   ```bash
   pip install selenium pandas matplotlib
   ```

4. Download ChromeDriver from [ChromeDriver downloads](https://chromedriver.chromium.org/downloads) and ensure it matches your Chrome version. Update the path in the code:

   ```python
   service = Service(executable_path=r"C:\Users\your-path-to-chrome-driver\chromedriver.exe")
   ```

5. Run the script using the command:

   ```bash
   python covid_data_scraper.py
   ```

## Usage

- The script automatically navigates to the specified CDC web pages, extracts relevant data, and plots the trends.
- Data is displayed in a line graph format, showing COVID-19 statistics over different weeks.

## Code Overview

The script performs the following tasks:

1. Initializes a headless Chrome WebDriver.
2. Defines the websites and selectors to scrape COVID-19 data.
3. Uses Selenium to extract text from the specified elements.
4. Processes the scraped data into a Pandas DataFrame.
5. Maps metrics to their respective selectors and prepares data for visualization.
6. Generates a line graph using Matplotlib to display the trends of COVID-19 statistics.

## Error Handling

The script includes basic error handling to catch timeouts and other exceptions during the scraping process. Messages will be printed to the console for any issues encountered.

## License

This project is open-source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any suggestions or improvements.

## Acknowledgements

- Thanks to the Selenium, Pandas, and Matplotlib communities for their resources and documentation.
