FROM pytorch/pytorch
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY dataset/Social_Network_Ads.csv Social_Network_Ads.csv
COPY src/init.py init.py
ENTRYPOINT ["python", "init.py"]
