FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1
RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential 
RUN mkdir /Nextner
WORKDIR /Nextner

COPY requirements.txt .
COPY entrypoint.sh .
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
COPY . .


ENTRYPOINT ["/Nextner/entrypoint.sh"]