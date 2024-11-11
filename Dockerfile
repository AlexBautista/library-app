FROM python:3.9-slim
WORKDIR /
COPY requirements.txt app.py models.py .
ADD templates .
RUN pip install -r requirements.txt
#https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues/58138250#58138250
CMD ["flask","run","--host", "0.0.0.0"]
