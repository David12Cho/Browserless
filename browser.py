# Selenium 4
from selenium import webdriver
import requests

def extract_title(website): #function to extract title from website input

    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability('browserless:token', '4b210727-4f5e-478f-a249-99f552e91a23')
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")

    driver = webdriver.Remote(
        command_executor='https://chrome.browserless.io/webdriver',
        options=chrome_options
    )
    driver.get(website)
    print(driver.title)
    driver.quit()

def web_scrape(website): #returns html script for website input
    # Define the payload with the required parameters
    payload = {
        'url': website,
        'apiKey': '4b210727-4f5e-478f-a249-99f552e91a23',
        'scroll': True,
        'waitFor': 5000
    }

    # Send a POST request to the Browserless API to initiate the scrape
    response = requests.post('https://chrome.browserless.io/scrape', json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the HTML content from the response
        html_content = response.json()['data']['html']
        # Do something with the HTML content
        print(html_content)
    else:
        # Handle any errors
        print('Error:', response.status_code, response.text)

def web_content(website): #returns html content for given website input
    api_key = "'4b210727-4f5e-478f-a249-99f552e91a23'"

    website_url = website

    # Construct the API URL with the website URL and API key
    api_url = f"https://chrome.browserless.io/screenshot?url={website_url}&access_token={api_key}"

    # Make a request to the API and get the response as a binary string
    response = requests.get(api_url).content

    # Save the response as an HTML file
    with open("website.html", "wb") as f:
        f.write(response)

    # Print the content of the website
        print(response.decode())


website = input("Please enter a website address: ")
extract_title(website)
web_scrape(website)


