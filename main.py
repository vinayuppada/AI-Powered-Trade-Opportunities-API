from fastapi import FastAPI, Header, HTTPException, Depends, Request
import requests
from groq import Groq
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import PlainTextResponse

# 🔑 Replace with your Groq API key
client = Groq(api_key="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")

app = FastAPI()

# ✅ Rate Limiter setup
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request: Request, exc):
    return PlainTextResponse("Too many requests. Please try later.", status_code=429)


# ✅ Authentication
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "secret123":
        raise HTTPException(status_code=401, detail="Unauthorized")


# ✅ Home route
@app.get("/")
def home():
    return {"message": "API is working"}


# ✅ Fetch data
def fetch_data(sector):
    try:
        url = f"https://duckduckgo.com/?q={sector}+india+market+news&format=json"
        response = requests.get(url)
        return response.text[:500]
    except Exception as e:
        return f"Error fetching data: {str(e)}"


# ✅ AI Report Generation
def generate_report(sector, data):
    try:
        prompt = f"""
        Analyze the {sector} sector in India.

        Based on this data:
        {data}

        Generate a professional markdown report with:

        # {sector.title()} Sector Report

        ## Overview
        ## Current Trends
        ## Opportunities
        ## Risks

        Keep it concise and structured.
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error from AI: {str(e)}"


# ✅ Main API Endpoint
@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
def analyze(request: Request, sector: str, auth=Depends(verify_api_key)):
    if not sector.isalpha():
        return {"error": "Invalid sector name"}

    data = fetch_data(sector)
    report = generate_report(sector, data)

    return {
        "sector": sector,
        "report": report
    }