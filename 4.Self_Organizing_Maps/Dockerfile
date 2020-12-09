FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /src/
WORKDIR /src/
RUN apt update
RUN apt install -y curl zip
RUN curl https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P16-Self-Organizing-Maps.zip --output zip.zip
RUN unzip zip.zip
CMD python3 learning.py
ENTRYPOINT ["python","learning.py"]
