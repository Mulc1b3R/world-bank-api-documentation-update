from bs4 import BeautifulSoup

# Read the content of the input wb-api-doc HTML file with the correct encoding
with open('SDMX API Queries – World Bank Data Help Desk.htm', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all <a> tags and update URLs that contain 'http://' to 'https://' within the anchor content
for a_tag in soup.find_all('a', href=True):
    if 'http://' in a_tag.contents[0]:
        a_tag.contents[0].replace_with(a_tag.contents[0].replace('http://', 'https://'))

# Save the modified HTML content back to the file
with open('SDMX API Queries – World Bank Data Help Desk.htm', 'w', encoding='utf-8') as file:
    file.write(str(soup))


# Script for Updating World Bank API Documentation Created by Psico Communications and Blockchain Development
# all rights reserved. 