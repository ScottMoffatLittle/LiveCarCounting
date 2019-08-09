FROM python:3

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils git htop wget nano curl

WORKDIR /vehicle_counting

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./detectors/* ./
COPY ./trackers/* ./
COPY ./utils/* ./
COPY Vehicle_Counting.py ./
COPY get_history ./
RUN chmod +x get_history.sh

ENTRYPOINT ["/vehicle_counting/get_history.sh"]
