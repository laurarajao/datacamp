FROM python:3.9-slim
RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 80
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]
