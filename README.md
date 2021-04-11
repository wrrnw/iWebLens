## Usage
### To run on local machine without Docker on Mac OS
Make sure you have **Python 3.5 or higher** and **pip** installed:
``` 
python3 --version
pip3 --version
```
Update and install package:
```
pip3 install --upgrade pip
pip3 install -r requirements.txt
```
Test detection with a sample image:
```
python3 object_detection.py yolo_tiny_configs/ inputfolder/000000473528.jpg 
```
To setup a server:
```
python3 iWebLens_server.py
```
Run detection with thread:
```
python3 iWebLens_client.py <inputfolder> <endpoint> <num_threads>
```
Here, **inputfolder** represents the folder that contains images for the test. The **endpoint** is the **REST API URL** and **num_threads** indicates the total number of threads sending requests to the server concurrently. 
For example:
```
python3 iWebLens_client.py inputfolder/ http://0.0.0.0:5000/api/object_detection 16
```

### To run on local machine with Docker installed
Fisrtly, open up a terminal and change directory into the iWebLens <br>
Then, build the iWebLens docker image by:
```
docker build -t iweblens .
```
Create a container from the image that just been created and enter the iteractive mode
```
docker run -it iweblens sh
```
Open up another terminal, type
```
docker ps
```
and then insert the container_id you get from the previous command
```
docker exec -it <container_id>
```
Test
```
python3 iWebLens_client.py inputfolder/ http://0.0.0.0:5000/api/object_detection 16
```
Done