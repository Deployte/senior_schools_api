from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI()

# Load JSON once when function is initialized
with open(os.path.join(os.path.dirname(__file__), "../senior_schools.json"), "r", encoding="utf-8") as f:
    schools = json.load(f)

@app.get("/api/schools")
def get_schools(county: str = None, gender: str = None, accommodation_type: str = None, regular_sne: str = None):
    filtered = schools
    if county:
        filtered = [s for s in filtered if s.get("county", "").lower() == county.lower()]
    if gender:
        filtered = [s for s in filtered if s.get("gender", "").lower() == gender.lower()]
    if accommodation_type:
        filtered = [s for s in filtered if s.get("accommodation_type", "").lower() == accommodation_type.lower()]
    if regular_sne:
        filtered = [s for s in filtered if s.get("regular_sne", "").lower() == regular_sne.lower()]

    if not filtered:
        return JSONResponse({"message": "No schools found matching the criteria."}, status_code=404)
    return filtered
