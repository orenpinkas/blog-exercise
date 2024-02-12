FROM python:3.12

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

EXPOSE 8000

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x ./entrypoint.sh

CMD ["bash", "entrypoint.sh"]

