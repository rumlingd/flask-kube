# Dockerised Flask API for Titanic Dataset With Postgres Database

### Docker Compose Build Instructions


This was built using the following versions

```sh
$ minikube version: v0.33.1
$ Docker version 18.09.1, build 4c52b90
$ docker-compose version 1.23.2, build 1110ad01
```

Build the three images and create containers using docker compose:

```sh
$ docker-compose up -d --build
```

Run the migrations and seed the postgres database with titanic csv:

```sh
$ docker-compose exec server python manage.py recreate_db
$ docker-compose exec server python manage.py seed_db
```

If you have errors in spinning any of the three containers to debug

```sh
$ docker events&
$ docker logs <copy the instance id from docker events messages on screen>
```

API Endpoints

1. [http://localhost:5001/api/v1/people](http://localhost:5001/api/v1/people) GET POST
1. [http://localhost:5001/api/v1/people/uuid](http://localhost:5001/api/v1/people/uuid) GET POST DELETE


To view the crude crud app visit http://localhost:8080 should possess same functionality as API


### Kubernetes

Ensure virtualisation is enabled in your bios and run the following commands

```sh
$ minikube start
$ sh deploy.sh
```

Allow Pods To Start. Belowe commands add minikube ip to your host file under hello.world
And seed the database.


```sh
$ echo "$(minikube ip) hello.world" | sudo tee -a /etc/hosts
$ POD_NAME=$(kubectl get pod -l service=postgres -o jsonpath="{.items[0].metadata.name}")
$ kubectl exec $POD_NAME --stdin --tty -- createdb -U sample people
$ FLASK_POD_NAME=$(kubectl get pod -l app=flask -o jsonpath="{.items[0].metadata.name}")
$ kubectl exec $FLASK_POD_NAME --stdin --tty -- python manage.py recreate_db
$ kubectl exec $FLASK_POD_NAME --stdin --tty -- python manage.py seed_db
```

To view the app visit http://hello.world/
