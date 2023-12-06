### Here's the python and docker implementation of our database app for CS223 project.

#### 0. Setup your python environment (virtual recommended)
```
python3 -m venv venv
source venv/bin/activate
(venv) pip install -r requirements.txt
```


#### 1. Setup three mysql database servers
```
docker-compose build
docker network create mynetwork
docker-compose up mysql_container_1 mysql_container_2 mysql_container_3 -d
```

This may not work so please check all container works with the following (on average run the following three times?)
```
docker-compose ps
docker-compose down
docker-compose up mysql_container_1 mysql_container_2 mysql_container_3 -d
```
If all three containers are working, then you are good to go.

#### 2. Run the following python code to initialize tables.
```
python3 initialize.py
```

#### 3. Initialize four users
```
cd db1
mysql -h 127.0.0.1 -P 3306 -u root -p < init_user.sql
```
Note: the password should be "root_password" as defined in docker-compose.yml


#### 4. Now you are ready to run all 7 transactions! You can run the following shell script to evaluate the throughput and latency

e.g
```
chmod +x run.sh
./run.sh
.....
```