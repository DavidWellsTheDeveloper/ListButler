FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /django_api
# Set the /django_recipe_api directory as the working directory
WORKDIR /django_api
# Copies from your local machine's current directory to the django_api folder 
# in the Docker image
COPY . .
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./requirements.txt /requirements.txt
# Install the requirements.txt file in Docker image
RUN pip install -r /requirements.txt
# Create a user that can run your container
RUN adduser -D user
USER user