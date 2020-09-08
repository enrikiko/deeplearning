FROM python:3
RUN apt-get install -y tree locate unzip vim
RUN pip3 install pillow Flask Werkzeug matplotlib pandas sklearn tensorflow Theano Flask
RUN pip3 install --upgrade keras
RUN mkdir /src/
WORKDIR /src/
RUN curl https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P16-Self-Organizing-Maps.zip --output zip.zip
RUN unzip zip.zip
CMD python3 learning.py
