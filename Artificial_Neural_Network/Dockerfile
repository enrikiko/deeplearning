FROM ubuntu
RUN apt-get update
RUN apt update
RUN apt install -y curl python3-pip
RUN apt-get install -y tree locate unzip vim
RUN pip3 install pillow Flask Werkzeug matplotlib pandas sklearn tensorflow Theano Flask
RUN pip3 install --upgrade keras
RUN updatedb
RUN mkdir -p deeplearning/Artificial_Neural_Network
WORKDIR deeplearning/Artificial_Neural_Network
COPY init.py init.py
COPY joke.py joke.py
COPY request.py request.py
COPY Churn_Modelling.csv Churn_Modelling.csv
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD sleep infinity
# RUN apt install -y curl
# RUN apt-get install tree
# RUN apt-get install locate
# RUN updatedb
# RUN bash Anaconda3-2019.03-Linux-x86_64.sh
#
# # #install anaconda
# RUN mkdir /tmp/anaconda
# RUN mkdir /tmp/spyder
# WORKDIR /tmp/anaconda
# RUN curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
# RUN sha256sum Anaconda3-2019.03-Linux-x86_64.sh
#
# FROM enriqueramosmunoz/rolling:papers
# RUN mkdir /tmp/spyder
# WORKDIR /tmp/spyder
#
#
# RUN apt-get -y install man
# # RUN pip3 install awscli --upgrade --user
# RUN apt install -y curl
# RUN apt install wget
#
# RUN apt install -y git
# # RUN git clone https://github.com/enrikiko/docker/
# RUN git clone https://github.com/enrikiko/Python/
# WORKDIR /tmp/spyder/Python/9.Intermediate/Spyder/Artificial_Neural_Networks/
# RUN source ~/.bashrc
# RUN conda install keras
# FROM enriqueramosmunoz/rolling:cigarettes
# COPY init.sh init.sh
#ENTRYPOINT [ "sh", "init.sh" ]




#
# RUN alias vault=ansible-vault
# RUN alias py=python
#
# RUN apt -y install awscli
# RUN curl -L -o /usr/local/bin/aws-vault https://github.com/99designs/aws-vault/releases/download/v4.2.0/aws-vault-linux-amd64
# RUN chmod 755 /usr/local/bin/aws-vault
# RUN apt-get -y install vim
