from bs4 import BeautifulSoup

# Read the content of the wb-api-doc HTML file with the correct encoding
with open('SDMX API Queries – World Bank Data Help Desk.htm', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags and update URLs that start with 'http://' to 'https://'
for a_tag in soup.find_all('a', href=True):
    if a_tag['href'].startswith('http://'):
        # Update 'http://' to 'https://'
        a_tag['href'] = a_tag['href'].replace('http://', 'https://')

# Save the modified HTML content back to the file
with open('SDMX API Queries – World Bank Data Help Desk.htm', 'w', encoding='utf-8') as file:
    file.write(str(soup))

# Script for Updating World Bank API Documentation Created by Psico Communications and Blockchain Development
# all rights reserved.    