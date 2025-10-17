# HNG 13 Backend Wizards - Stage 0 Task

## Description
This project is a simple Flask RESTful API that returns my profile information along with a dynamic cat fact fetched 
from an external API.                                                                                                                                                
It has two endpoints:
- `/` → Redirects users automatically to `/me`
- `/me` → Displays the profile data, a random cat fact, and the current timestamp.


Project goals
- Building a simple REST API
- Consuming third party APIs with the current timestamp in UTC ISO 8601 format
- Fetching random cat fact from the Cat Facts API
- Returning dynamic JSON data

## API ENDPOINT
**GET** "/me"
**Response Example:**
{
  "fact": "Many cats love having their forehead gently stroked.",
  "status": "success",
  "timestamp": "2025-10-17T19:56:32.573943+00:00",
  "user": {
    "email": "ezerichard100@gmail.com",
    "name": "Richard Eze Arinze",
    "stack": "Python, Flask"
  }
}
## Local Setup Instructions
1. Clone the Repository:
git clone https://github.com/Richardeze/HNG_Stage_0.git
cd HNG_Stage_0
2. Create a Virtual Environment:
python3 -m venv .venv
source .venv/bin/activate
3. Install Dependencies:
pip install -r requirements.txt
4. Run the Application: python main.py
5. Access the application: Visit http://127.0.0.1:5000/me