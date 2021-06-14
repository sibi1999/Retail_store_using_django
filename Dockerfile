FROM python:3.9
COPY . .
RUN pip install --no-cache-dir django
RUN pip install --no-cache-dir Pillow 
RUN pip install --no-cache-dir djongo
RUN pip install --no-cache-dir pymongo
RUN pip install  --no-cache-dir pymongo[srv]

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

