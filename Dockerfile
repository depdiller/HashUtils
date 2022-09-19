FROM python:3.9

WORKDIR /usr/src/app

COPY libraries.txt ./

RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r libraries.txt

COPY . .

CMD ["python", "./app.py"]