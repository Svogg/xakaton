FROM python:3.11.1

WORKDIR /xakaton/backend

COPY backend/requirements.txt .

RUN pip3 install --upgrade pip

RUN pip3 install -r requirements.txt --no-cache-dir

COPY backend/entity_endpoints ./

EXPOSE 8000