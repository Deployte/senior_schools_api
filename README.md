# Kenya Senior Schools API 

An API for querying and filtering a dataset of senior schools in Kenya.  
This project is built using **FastAPI** and is deployed as a **Serverless Function** on **Vercel**.

---

##  Features
- Filter schools by various criteria, including:
  - County
  - Gender
  - Accommodation type
  - School name
  - Regular vs. Special Needs (SNE)
- Retrieve a single school's details by its unique **KNEC code** or **UIC**.
- Fast and efficient data access by loading the dataset into memory at startup.

---

## Technologies Used
- **FastAPI**: Modern, fast web framework for building APIs with Python 3.7+.
- **Python**: Core programming language.
- **Vercel**: Platform for instant, zero-configuration deployment of serverless functions.

---

##  API Endpoints

**Base URL:**  
https://senior-schools-api.onrender.com/

---

### 1. Filter Schools
**Endpoint:** `/api/schools`  
**Method:** `GET`  
**Description:** Use query parameters to filter the list of schools. All parameters are optional.

| Parameter            | Example Value  | Description                                |
|----------------------|----------------|--------------------------------------------|
| `county`             | Nairobi        | Filters schools by county.                 |
| `gender`             | boys / girls   | Filters schools by gender.                 |
| `accommodation_type` | boarding / day | Filters by accommodation type.             |
| `regular_sne`        | regular / sne  | Filters for Special Needs Education.       |
| `name`               | starehe        | Case-insensitive search in school name.    |

**Example Usage:**

- API Endpoint:
GET /api/schools?county=Nairobi&gender=boys

- In a browser:
 [https://senior-schools-api.onrender.com/api/schools?county=Nairobi&gender=boys](https://senior-schools-api.onrender.com/api/schools?county=Nairobi&gender=boys)

### 2. Get a Single School
**Endpoint:** `/api/school/{id}`  
**Method:** `GET`  
**Description:** Fetches a single school by its unique **KNEC code** or **UIC**.

**Example Usage:**

- API Endpoint:
GET /api/school/33517209
GET /api/school/7J98


- In a browser:
  [https://senior-schools-api.onrender.com/api/school/33517209](https://senior-schools-api.onrender.com/api/school/33517209)


## Local Development

### Prerequisites
- Python 3.7 or higher

### 1. Clone the Repository
```bash
git clone https://github.com/Deployte/senior_schools_api.git
cd senior_schools_api

```
### 2. Install Dependencies
It is recommended to use a virtual environment.

```bash

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

# Install the required packages
pip install -r requirements.txt

```
### 3. Run the Server
Start the local development server using uvicorn.

```bash
uvicorn api.app:app --reload

```
- Your API will now be running locally at http://127.0.0.1:8000. 
- You can access the API documentation (Swagger UI) at http://127.0.0.1:8000/docs.










