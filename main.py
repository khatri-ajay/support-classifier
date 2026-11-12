from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


class Ticket(BaseModel):
    message: str


@app.post("/classify")
def classify(ticket: Ticket):
    message = ticket.message.lower()

    if "refund" in message:
        category = "billing"
    elif "error" in message:
        category = "technical"
    else:
        category = "general"

    return {
        "category": category,
        "service": os.getenv("SERVICE_NAME", "Customer Support")
        }