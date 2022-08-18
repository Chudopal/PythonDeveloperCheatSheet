FROM python:3.10
COPY . /docker_hw
ENV os_secret_key="ngw$o&)i=7j!=n=a7ej3qaj#bv%-n(4ac6e%nhbth%8*c2kz!b"
WORKDIR /docker_hw
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
EXPOSE 5000
