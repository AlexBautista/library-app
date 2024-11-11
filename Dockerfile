FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
#CMD ["python", "app.py"]
#https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues/58138250#58138250
#ENV FLASK_APP=app.py
CMD ["flask","--app app", "run", "--host", "0.0.0.0"]
