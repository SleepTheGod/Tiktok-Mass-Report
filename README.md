# TikTok Mass Report Bot

This repository contains a script to mass report TikTok users using proxies fetched from ProxyScrape. The script automates the process of reporting users without requiring an API key by interacting directly with TikTok's web interface using Selenium.

## Features

- **Proxy Rotation**: Dynamically fetches and rotates through a list of proxies from ProxyScrape.
- **Selenium Automation**: Uses Selenium WebDriver to automate reporting actions on TikTok's web interface.
- **Customizable**: Easily update user IDs and report reasons.

## Requirements

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- [ProxyChains](https://github.com/haad/proxychains)
- Python packages: `selenium`, `requests`, `webdriver-manager`

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/SleepTheGod/Tiktok-Mass-Report.git
    cd Tiktok-Mass-Report
    ```

2. **Install the required Python packages:**

    ```sh
    pip install selenium requests webdriver-manager
    ```

3. **Install Google Chrome and ChromeDriver:**

    - [Download Google Chrome](https://www.google.com/chrome/)
    - [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) and ensure it is in your PATH.

4. **Install ProxyChains:**

    On Ubuntu or Debian-based systems:

    ```sh
    sudo apt-get install proxychains
    ```

    Ensure your `proxychains.conf` file is correctly configured. You may need to adjust the path in the script if necessary.

## Usage

1. **Update the script with the user ID and reason:**

    Edit `report.py` and replace the following placeholders with the actual values:
    
    ```python
    user_id = '1234567890'  # Replace with the actual user ID
    report_reason = 'Violation of community guidelines'  # Replace with the actual reason for reporting
    ```

2. **Run the script:**

    ```sh
    python report.py
    ```

    The script will:
    - Fetch proxies from ProxyScrape.
    - Set up Selenium WebDriver to use each proxy.
    - Navigate to the specified TikTok user's page.
    - Automate the reporting process.

## Notes

- Ensure the XPath selectors in `report.py` match the actual elements on TikTok's site. These can change, so you might need to inspect the page and update the selectors accordingly.
- This script assumes you have Chrome installed and are using ChromeDriver. Adjust accordingly for other browsers.
- Be mindful of TikTok's terms of service when using automation tools.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
