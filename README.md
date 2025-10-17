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


## Dependencies
This project uses the following main dependencies:
- **Flask** – for creating the RESTful API
- **Requests** – for fetching data from the Cat Facts API
- **python-dotenv** – for handling environment variables

All dependencies are listed in the `requirements.txt` file and can be installed with:
pip install -r requirements.txt


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

## Example Response 
A sample response from the /me endpoint:

{
  "status": "success",
  "user": {
    "email": "ezerichard100@gmail.com",
    "name": "Richard Eze Arinze",
    "stack": "Python, Flask"
  },
  "timestamp": "2025-10-17T18:05:41.213186+00:00",
  "fact": "Cheetahs do not roar, as the other big cats do. Instead, they purr."
}
