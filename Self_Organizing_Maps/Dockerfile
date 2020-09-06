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
RUN curl https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/P16-Self-Organizing-Maps.zip --output zip.zip
RUN unzip zip.zip
RUN pip3 install pandas
RUN pip3 install matplotlib
RUN pip3 install sklearn
#?RUN pip3 install matplotlib
RUN cp Self_Organizing_Maps/minisom.py minisom.py
