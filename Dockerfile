FROM python:3.11.8-alpine3.19
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN alembic init migrations && cp env.py ./migrations/

