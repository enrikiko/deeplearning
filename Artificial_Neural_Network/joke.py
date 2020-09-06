import time
def save(info):
    file=str(time.time())
    file='tmp/'+file
    with open(file, "a") as f:
        f.write(info+"\n")
