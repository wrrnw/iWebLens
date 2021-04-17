## Usage

---
### To run on local machine without Docker installed on Mac OS
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

Test detection with a sample image, make sure you are in the project folder and run:
```
python3 given_resources/object_detection.py yolo_tiny_configs/ inputfolder/000000473528.jpg 
```

To setup a server:
```
python3 iWebLens_server.py
```

Keep the server terminal open and open another terminal, run detection with thread:
```
python3 iWebLens_client.py <inputfolder> <endpoint> <num_threads>
```

Here, **inputfolder** represents the folder that contains images for the test. The **endpoint** is the **REST API URL** and **num_threads** indicates the total number of threads sending requests to the server concurrently.

For example:
```
python3 iWebLens_client.py inputfolder/ http://0.0.0.0:5000/api/object_detection 16
```


---
### To run on local machine without Docker installed on Ubuntu 18.04

Firstly, install **python 3.5 or higher**, **pip** and **opencv**
```
sudo apt-get update
sudo apt-get install -y python python3-pip python3-opencv
```

Make sure you have successfully install the packages
```
python3 --version
pip3 --version
```

Update and install python libraries:
```
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

Test detection with a sample image, make sure you are in the project folder and run:
```
python3 given_resources/object_detection.py yolo_tiny_configs/ inputfolder/000000473528.jpg 
```

To setup a server:
```
python3 iWebLens_server.py
```

Keep the server terminal open and open another terminal, run detection with thread:
```
python3 iWebLens_client.py <inputfolder> <endpoint> <num_threads>
```

Here, **inputfolder** represents the folder that contains images for the test. The **endpoint** is the **REST API URL** and **num_threads** indicates the total number of threads sending requests to the server concurrently. 
For example:
```
python3 iWebLens_client.py inputfolder/ http://0.0.0.0:5000/api/object_detection 16
```


---
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

Open up another terminal, then type the command to get the process id:
```
docker ps
```

and then insert the container_id you get from the previous command
```
docker exec -it <container_id> sh
```

Test
```
python3 iWebLens_client.py inputfolder/ http://0.0.0.0:5000/api/object_detection 16
```

---
### Install kind and kubectl into Ubuntu 18.04
Install kind and put it into the $PATH
```
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.10.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

Check if it is installed successfully:
```
kind --version
```

Similarly, install kubectl and put it into the $PATH
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
chmod +x ./kubectl
sudo mv ./kubectl /usr/local/bin/kubectl
```

Check if it is installed successfully:
```
kubectl version --client
```

Create a cluster with pre-built node image and customised configuration file:
```
sudo kind create cluster --config kind-config.yaml
```

To get the nodes info:
```
sudo kubectl get nodes -o wide
```

Create Deployment and Service using customised configuration file:
```
sudo kubectl apply -f k8s-config.yaml
```

To see if the pods and services created successfully:
```
sudo kubectl get all -o wide
```

To scale up or scale down the number of the pods in the deployment:
```
kubectl scale deployment iweblens-deployment --replicas=4
```

To delete the created deployment and service:
```
kubectl delete -f iweblens-deployment
```

To delete the cluster:
```
sudo kind delete cluster
```
