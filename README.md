# Project Title

This project is a simple FastAPI application that provides student information through an API endpoint.

## Setup Instructions

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Anuoluwapo25/HNG-Stage1

    cd HNG-Stage1
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```
    

4. **Run the application**:
    ```
    python manage.py runserver
    ```

## API Documentation

### Endpoint URL

- **GET** `<your-domain.com>/api/classify-number?number=371`

### Response Format

- **Response(200 OK)**:
    ```json
            "data":{
            "number": "371",
            "is_prime": "false",
            "is_perfect": "false",
            "properties": ["armstrong", "odd"],
            "digit_sum": "11", 
            "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
        },
        
    ```
- **Response(400 bad request)**:

    ```json
                {
                "number": "alphabet",
                "error": true
            },
    ```


### Example Usage

To get the user information, send a GET request to the `/` endpoint. You can use `curl` or any API client like Postman.

```sh
curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
```