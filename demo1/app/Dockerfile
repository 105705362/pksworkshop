FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip install Flask
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 5000:5000

CMD [ "python", "./quickstart.py" ]
#CMD [ "sh", "./start-server.sh" ]
#CMD [ "python", "./start-server.py" ]
