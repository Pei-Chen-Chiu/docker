FROM python:3.7
WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000
COPY . .
CMD ["flask", "run"]