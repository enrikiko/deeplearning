FROM pytorch/pytorch
RUN python -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY dataset/ml-1m/movies.dat movies.dat
COPY dataset/ml-1m/users.dat users.dat
COPY dataset/ml-1m/ratings.dat ratings.dat
COPY dataset/ml-100k/u1.base u1.base
COPY dataset/ml-100k/u1.test u1.test
COPY src/init.py init.py
ENTRYPOINT ["python", "init.py"]
