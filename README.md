# Getting Started
##  Prerequisites
- Python 3.x
- pip

##  Installation
1.  Clone the repository to your local machine:
```git clone <repository_url>```

2.  Cd to server foler:
```cd server```

3.  Create a virtual environment:
```python3 -m venv .venv```

4.  Activate the virtual environment: 
    -   For Unix/Linux:
        ```source .venv/bin/activate```
    -   For Windows:
        ```.venv\Scripts\activate```
5.  Install the project dependencies:
```pip install -r requirements.txt```

6.  Apply migrations:
```python manage.py migrate```

7.  Start the development server:
```python manage.py runserver```
The development server should now be running at http://localhost:8000.

#   Usage
-   You can now start developing your Django project using the virtual environment. Make sure to activate the virtual environment every time you work on the project:
```source .venv/bin/activate```
-   To deactivate the virtual environment, simply run:
```deactivate```

# Getting Started on build docker
Follow the instructions below to set up and run the Django project using Docker.

1. Clone the repository to your local machine:
```git clone <repository_url>```

2. Cd to server folder
```cd server```

3. Build the Docker image:
```docker build -t homiracle_ml .```

4. Run the Docker container:    
```docker run -d -p 8000:8000 homiracle_ml```

5. Access the Django application:
Open your web browser and navigate to http://localhost:8000. You should see the Django application running.