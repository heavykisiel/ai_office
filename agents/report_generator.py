from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_report(trend_insights, product_recommendations):
    prompt = f"Summarize the following insights:\n\nTrends:\n{trend_insights}\n\nProducts:\n{product_recommendations}"
    response = client.chat.completions.create(model="o1-mini",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content

