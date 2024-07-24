FROM python:latest

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["source"]
CMD [".venv/bin/activate"]

ENTRYPOINT ["reflex"]
CMD ["db", "makemigrations"]

ENTRYPOINT ["reflex"]
CMD ["db", "migrate"]

ENTRYPOINT ["reflex"]
CMD ["run"]