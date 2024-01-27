import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

def scrape_website(url):
    # Make an HTTP request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract data from the HTML (replace this with your own scraping logic)
        # For example, extracting all the links on the page
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        return links
    else:
        # If the request was not successful, return an empty list or handle the error
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    if request.method == 'POST':
        # Get the URL input from the form
        url = request.form['url']
        
        # Call the scrape_website function with the provided URL
        scraped_data = scrape_website(url)
        
        # Render the template with the scraped data
        return render_template('result.html', data=scraped_data)

if __name__ == '__main__':
    app.run(debug=True)
