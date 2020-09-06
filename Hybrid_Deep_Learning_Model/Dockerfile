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
COPY ./init.py ./init.py
CMD python3 init.py
