FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/personal_website

COPY requirements.txt /app/personal_website/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/personal_website/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

