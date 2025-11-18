




from fastapi import FastAPI
from routes import deals, users

app = FastAPI(title="Smart Deal Tracker API")

app.include_router(deals.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"status": "ok", "message": "Smart Deal Tracker API running"}
