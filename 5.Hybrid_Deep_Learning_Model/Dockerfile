FROM python:3.8-slim
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN apt update
RUN apt install -y curl zip
RUN curl https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P16-Self-Organizing-Maps.zip --output zip.zip
RUN unzip zip.zip
COPY src /src
RUN mv /Self_Organizing_Maps/* /src/
WORKDIR /src/
CMD python init.py
ENTRYPOINT ["python", "init.py"]
