This project is based on the work from:
git@github.com:nicholaskajoh/Vehicle-Counting.git

It pulls the stream of live traffic cameras from the I-66 freeway in Virginia and runs YOLO object detection and CSRT tracker to record the speed and throughput of cars. It was designed to be an input to my TollPrediction model running on Kinetica. The results of the model are pushed into Kinetica's DB, and images of each detected car is stored in Minio object storage.
