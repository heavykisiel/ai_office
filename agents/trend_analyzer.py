from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def fetch_trends():
    # Mock example; replace with real data fetching (e.g., Google Trends API)
    return ["digital value"]

def analyze_trends(trends):
    prompt = f"Analyze the following trends and suggest profitable niches: {', '.join(trends)}"
    response = client.chat.completions.create(model="o1-mini",
    messages=[{"role": "user", "content": prompt}])
    return response.choices[0].message.content

