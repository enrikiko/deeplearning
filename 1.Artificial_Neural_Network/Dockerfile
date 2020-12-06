FROM python:3.8-slim
COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
# RUN pip3 install requests pillow Flask Werkzeug matplotlib pandas sklearn tensorflow Theano
# RUN pip3 install --upgrade keras
RUN mkdir -p deeplearning/Artificial_Neural_Network
WORKDIR deeplearning/Artificial_Neural_Network
COPY src/init.py init.py
COPY src/functions.py functions.py
COPY data/Churn_Modelling.csv Churn_Modelling.csv
CMD sleep infinity
ENTRYPOINT ["python","init.py"]
