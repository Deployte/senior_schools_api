from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import json
import os

app = FastAPI(title="Schools API", version="1.2.0")

# Load dataset once (improves speed)
DATA_FILE = os.path.join(os.path.dirname(__file__), "../senior_schools.json")
with open(DATA_FILE, "r", encoding="utf-8") as f:
    SCHOOLS = json.load(f)


@app.get("/api/schools")
async def get_schools(
    county: str | None = Query(None),
    gender: str | None = Query(None),
    accommodation_type: str | None = Query(None),
    regular_sne: str | None = Query(None),
    name: str | None = Query(None),
):
    """Filter schools by query parameters"""
    filtered = SCHOOLS

    if county:
        filtered = [s for s in filtered if s.get("county", "").lower() == county.lower()]
    if gender:
        filtered = [s for s in filtered if s.get("gender", "").lower() == gender.lower()]
    if accommodation_type:
        filtered = [
            s for s in filtered
            if (s.get("accommodation_type") or s.get("accomodation_type", "")).lower() == accommodation_type.lower()
        ]
    if regular_sne:
        filtered = [s for s in filtered if s.get("regular_sne", "").lower() == regular_sne.lower()]
    if name:
        filtered = [s for s in filtered if name.lower() in s.get("school_name", "").lower()]

    if not filtered:
        return JSONResponse(status_code=404, content={"message": "No schools found"})
    return filtered


@app.get("/api/school/{id}")
async def get_school(id: str):
    """
    Fetch a single school by its KNEC code or UIC.
    Example:
      - /api/school/33517209   (KNEC)
      - /api/school/7J98       (UIC)
    """
    school = next(
        (s for s in SCHOOLS if str(s.get("knec")) == id or str(s.get("uic")).lower() == id.lower()),
        None,
    )

    if not school:
        return JSONResponse(status_code=404, content={"message": f"School with ID '{id}' not found"})
    return school
