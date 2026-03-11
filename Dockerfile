FROM python:3
LABEL maintainer="Quinn Henry"

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY scraper.py ./
COPY entrypoint.sh ./

# Install dependencies
RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]

RUN ["chmod", "+x", "entrypoint.sh"]

CMD ["/usr/src/app/entrypoint.sh"]