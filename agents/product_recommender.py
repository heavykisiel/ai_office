# agents/product_recommender.py
from openai import OpenAI

import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from bs4 import BeautifulSoup
import requests


def scrape_store(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    products = [item.text for item in soup.find_all('h2', class_='product-title')]
    return products

def recommend_products(products):
    prompt = f"Based on these products: {', '.join(products)}, suggest products to sell."
    response = client.chat.completions.create(model="o1-mini",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content

