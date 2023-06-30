FROM pypy:latest

RUN mkdir /app/

EXPOSE 8000

COPY . /app/

WORKDIR /app/

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]