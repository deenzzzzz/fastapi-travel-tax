from fastapi import FastAPI
from fastapi_travel_tax.routes import tax_routes

app = FastAPI()
app.include_router(tax_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to Travel Tax API"}