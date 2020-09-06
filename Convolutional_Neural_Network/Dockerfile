FROM ubuntu
RUN apt-get update
RUN apt update
RUN apt install -y curl python3-pip
RUN apt-get install -y tree locate unzip vim
RUN pip3 install pillow Flask Werkzeug matplotlib pandas sklearn tensorflow Theano Flask
RUN pip3 install --upgrade keras
RUN updatedb
RUN mkdir /src/
WORKDIR /src/
RUN curl https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P16-Convolutional-Neural-Networks.zip --output zip.zip
RUN unzip zip.zip
RUN cp -r Convolutional_Neural_Networks/dataset ./
RUN rm -r zip.zip Convolutional_Neural_Networks/ __MACOSX/
COPY ./src/ /src/
CMD python3 learning.py
