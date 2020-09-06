FROM ubuntu
RUN apt update
RUN apt-get update
RUN apt install -y curl
RUN apt install -y python3-pip
RUN apt install -y git
RUN apt-get install tree
RUN apt-get install locate
RUN apt-get install unzip -y
RUN pip3 install tensorflow
RUN pip3 install --upgrade keras
RUN pip3 install Theano
RUN pip3 install pillow
RUN pip3 install Werkzeug
RUN pip3 install Flask
RUN updatedb
RUN mkdir /src/
WORKDIR /src/
RUN curl https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P16-Convolutional-Neural-Networks.zip --output zip.zip
RUN unzip zip.zip
RUN cp -r Convolutional_Neural_Networks/dataset ./
RUN rm -r zip.zip Convolutional_Neural_Networks/ __MACOSX/
COPY ./src/ /src/
CMD python3 learning.py
