FROM python:3

WORKDIR /usr/src/milletContainer

COPY pip-requirements.txt ./
RUN pip3 install --no-cache-dir -r pip-requirements.txt

COPY . .

CMD [ "python3", "manage.py","runserver" ]