from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Quantitative Trading Model API"}

# Add more endpoints as needed
