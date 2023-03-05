# Log Parser

## Problem
This solution is built to automate the quality control evaluation of the home sensors. Evaluation criteria is as follows:
- For a thermometer, it is branded “ultra precise” if the mean of the readings is within 0.5 degrees of the known temperature, and the standard deviation is less than 3. It is branded “very precise” if the mean is within 0.5 degrees of the room, and the standard deviation is under 5. Otherwise, it’s sold as “precise”.
- For a humidity sensor, it must be discarded unless it is within 1 humidity percent of the reference value for all readings. (All humidity sensor readings are a decimal value representing percent moisture saturation.)

## Solution
In order to solve the problem, I have developed a (python) script to parse the logs from the devices and classify based on the evaluation criteria mentioned above. Then, script is bundled as a docker image to run on distributed environments. Also, it's packaged using helm to ease deployment and management on various kubernetes environments.

Since it can run on kubernetes, script is integrated with an API using "Flask" to make it available for the other applications.

### Docker Build
Here are the steps to build the docker image:

```
docker build --network host -t log-parser:v0.1 .
docker tag log-parser:v0.1 gulere/log-parser:v0.1
docker push gulere/log-parser:v0.1
```
For easier testing, image is stored at docker.io.

### Helm 
Using the docker image built above, Helm charts is created. 
To deploy the charts, clone the repository and under 'helm' directory, run:
```
helm install log-parser .
```
By default, it runs with 1 replica, but can be increased by the 'replicaCount:' in 'values.yaml', then
```
helm upgrade log-parser
```

### Test
Solution can be tested using either API or running respective python script manually.

#### Using API
##### Using Sample file
![Local Sample](https://github.com/gulererdinc/log-parser/blob/main/img/local-api.png?raw=true)
##### File Upload (on Kubernetes)
![K8s Upload](https://github.com/gulererdinc/log-parser/blob/main/img/remote-api.png?raw=true)
#### Manual Execution
![Manual](https://github.com/gulererdinc/log-parser/blob/main/img/local-api.png?raw=true)


