FROM pypy:latest
RUN pip3 install requests spacy
WORKDIR /app
COPY . /app
CMD python garden.py