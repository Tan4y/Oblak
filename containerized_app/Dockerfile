FROM python:3.9
# FROM python:3.9: Sets the base image to python:3.9, which provides a Python 3.9 environment.
# Using a specific version (like 3.9) ensures compatibility and consistency for Python code
# in the container.
WORKDIR /app
# WORKDIR /app: Sets the working directory to /app.
# This means all subsequent commands (like file copying or command execution) will run from
# this directory. If /app does not exist, it will be created automatically.
COPY requirements.txt .
# COPY requirements.txt .: Copies the requirements.txt file from the host machine into the
# container’s working directory (/app). This file typically lists the Python dependencies required
# for the application.
COPY app/ ./app
# COPY app/ ./app: Copies the entire app/ directory from the host to the /app/app directory
#  in the container. This directory likely contains the main application code.
COPY app/templates/ ./templates
# COPY app/templates/ ./templates: Copies the app/templates/ directory from the host to the
# /app/templates directory in the container. This directory contains HTML templates,
# such as index.html, which Flask will use to render web pages.
COPY db/ /db 
# COPY db/ /db: Copies the db/ directory from the host into the /db directory in the container.
# This may contain database scripts, like initialize_db.py.
RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt: Installs Python dependencies listed in requirements.txt.
# The --no-cache-dir option prevents caching of the packages, which reduces the size of the Docker image.
EXPOSE 5000
# EXPOSE 5000: Opens port 5000 in the container. This allows network traffic on port 5000,
# which is commonly used by Flask apps to serve web content. It doesn’t automatically map the port
# to the host, but it allows other services to connect to it.
CMD ["python", "app/app.py"]
# CMD ["python", "app/app.py"]: Specifies the command to run when the container starts.
# Here, it runs the Flask application by executing app.py located in the /app/app directory.
# This is the main entry point for the application.