from flask import Blueprint, jsonify, request
import requests
from bs4 import BeautifulSoup

scraper_bp = Blueprint('scraper', __name__)

@scraper_bp.route('/scrape', methods=['POST'])
def scrape_data():
        url = request.json.get('url')
        
        if not url:
            return jsonify({"error": "URL not provided"}), 400

        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            article_titles = soup.find_all("h2")
            
            titles = [title.text.strip() for title in article_titles]
            return jsonify({"titles": titles})
        else:
            return jsonify({"error": "Failed to get data"}), 500
