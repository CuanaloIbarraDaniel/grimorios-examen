# Start from the official Python base image.
FROM python:3.12

# Set the current working directory to /code
WORKDIR /code

# Copy the file with the requirements to the /code directory
COPY requirements.txt /code/requirements.txt

# Install the package dependencies in the requirements file.
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the ./app directory inside the /code directory
COPY ./grimorios /code/app

# Set the command to use fastapi run, which uses Uvicorn underneath.
CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "80"]