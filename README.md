## Setup Instructions
### 1. Clone the repsitory:
    ###First clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/hello_django.git

### 2. Navigate to the project folder:
    cd hello_django

### 3. Create a virtual environment:
    python -m venv venv

### 4. Activate a virtual environment:
    ### Windows:
    .\venv\Scripts\activate

    ### Mac/Linux:
    source venv/bin/activate

### 5. Install dependencies:
    ### Install the required packages from requirements.txt
    pip install -r requirements.txt

### 6. Run the Django server:
    ### Start the server by running the following command:
    python manage.py runserver 8001

### 7. Access the application:
    ### JSON Response: Visit 
    http://127.0.0.1:8001/json/

    ###Expected output: {"Message": "Hello World!"}

    ### HTML Response: Visit
    http://127.0.0.1:8001/html/

    ###Expected output: "Hello World!" in bold.