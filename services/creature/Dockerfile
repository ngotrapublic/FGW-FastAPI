FROM python:3.13.1

WORKDIR /

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY . .

CMD ["python", "creature.py"]
