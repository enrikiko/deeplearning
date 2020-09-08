FROM python:3
RUN apt-get install -y tree locate unzip vim
RUN pip3 install pillow Flask Werkzeug matplotlib pandas sklearn tensorflow Theano Flask
RUN pip3 install --upgrade keras
RUN mkdir /src/
COPY ./dataset/ /src/
COPY ./src/init.py /src/
RUN updatedb
WORKDIR /src/
CMD python3 init.sh
#ENTRYPOINT ["./init.sh"]
