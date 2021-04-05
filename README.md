## Usage
### Mac OS
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
python3 web_service.py
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