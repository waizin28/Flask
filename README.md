## Getting Started

First, create a virtual environment and activate it using the following commands:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

Note: From VScode, to choose python interpreter: Command + Shift + P (Mac) or Conrtol + Shift + P (Window)
Choose python version that has path to ./.venv/bin/python

Afterward, download the required libraries to run this app from requirements.txt

```bash
pip install -r requirements.txt
```

2 ways to run this app:

To create and run docker image (Make sure you have installed docker CLI)

```
docker build -t flask-api .
docker run -p 5005:5000 flask-api -w /app -v "$(pwd):/app" flask-api
```

Or run the following command to start the server:

```bash
flask run
```

Go to "http://127.0.0.1:5000/swagger-ui" to interact with the endpoints (this will take you to Swagger UI)

## Cleaning Up

Please deactivate the virtual environment by typing "deactivate" at the console.

If you installed any new libraries, please use "pip freeze > requirements.txt" to edit to requirements.txt file.
# Flask
