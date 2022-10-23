FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
