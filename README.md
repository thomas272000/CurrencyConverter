# CurrencyConverter

A Django REST API that performs currency conversions using live exchange rates. Users can
convert currencies and view recent conversions.

# Features
- Convert an amount from one currency to another using live exchange rates.
- Retrieve the last 5 conversion records.
- Error handling for invalid API requests and currency codes.


# Technologies Used
- Django: Backend framework.
- Django REST Framework: For building REST API endpoints.
- Requests: For making HTTP requests to an external currency API.


# API_URL = 'https://v6.exchangerate-api.com/v6/d84978a6f65de1281f2b766c/latest/'


# Setup and Installation

Clone the repository:
   ```bash
   git clone 
   cd blood-bank-management
   python3 -m venv venv
   source venv/bin/activate 
   pip install -r requirements.txt
   Configure Environment Variables
   Create a .env file in the project root to securely store environment variables like your API key.
 ```
 EXCHANGE_API_KEY=your_actual_api_key_here

   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

  NOTE : USE POSTMAN OR THUNDERCLIENT TO CHECK API

  

# API Endpoints
# BaseURL: http://127.0.0.1:8000/
1. Convert Currency
 - URL: BaseURL/convert
 - Method: POST
 - Request Body:
```
 #pass this as JSon data

 {
 "from_currency": "USD",
 "to_currency": "EUR",
 "amount": 100
 }
 ```

  # Response:
 ```
 {
 "id": 1,
 "from_currency": "USD",
 "to_currency": "EUR",
 "amount": 100,
 "converted_amount": 92.34,
 "rate": 0.9234,
 "date": "2023-01-01T12:00:00Z"
 }
 ```

 2. Get Conversion History
 - URL: BASEURL/history
 - Method: GET
 


 # Response- LAST 5 data
 [
 {
 "id": 1,
 "from_currency": "USD",
 "to_currency": "EUR",
 "amount": 100,
 "converted_amount": 92.34,
 "rate": 0.9234,
 "date": "2023-01-01T12:00:00Z"
 },
 ...
 ]
 


3. Get Live Exchange Rate
 - URL: BASEURL/live
 - Method: GET
 


 # Response

 {
    "base_currency": "USD",
    "conversion_rates": {
        "USD": 1,
        "AED": 3.6725,
        "AFN": 66.4895,
        "ALL": 91.3161,
        "AMD": 387.9199
        etc...
    }
    }
 

