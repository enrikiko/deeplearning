FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /src/
WORKDIR /src/
RUN apt update
RUN apt install -y curl
RUN curl https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P16-Convolutional-Neural-Networks.zip --output zip.zip
RUN apt install -y zip
RUN unzip zip.zip
COPY src/learning.py learning.py
RUN mv Part\ 2\ -\ Convolutional\ Neural\ Networks/dataset/* ./
RUN rm -r  Part\ 2\ -\ Convolutional\ Neural\ Networks/dataset/
CMD sleep infinity
ENTRYPOINT ["python", "learning.py"]
