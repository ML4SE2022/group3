FROM ubuntu:22.04

WORKDIR /gr3/

RUN apt-get update -q &&\
    apt-get install -q -y python3 python3-pip

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY fine_tuning fine_tuning
COPY train_test_data train_test_data

WORKDIR /gr3/fine_tuning/

ENTRYPOINT [ "python3", "train_and_test.py" ]
