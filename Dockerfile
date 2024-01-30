FROM python:3.10

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt ./ 
RUN pip install --no-cache -r requirements.txt

COPY ./pycode/ ./

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
