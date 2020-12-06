FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y tree locate unzip vim
RUN mkdir /src/
COPY ./dataset/ /src/
COPY ./src/init.py /src/
RUN updatedb
WORKDIR /src/
CMD python3 init.sh
ENTRYPOINT ["python","init.py"]
