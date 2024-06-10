FROM python:3.11-slim

RUN apt-get update && apt-get install -y pkg-config && apt-get install -y libhdf5-dev

WORKDIR /appcode

RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  software-properties-common \
  git \
  && rm -rf /var/lib/apt/lists/*

# RUN mkdir /requirements
# COPY ./src/requirements.txt /requirements/requirements.txt

COPY ./src/requirements.txt .

RUN pip3 install -r requirements.txt

RUN ls

EXPOSE 8501

# HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# ENTRYPOINT ["streamlit", "run", "src/Home.py", "--server.port=8501", "--server.address=0.0.0.0"] 

CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
