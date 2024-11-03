# real-time-analytics

The purpuse of the project is to process and monitor real-time data from production processes.

## Prerequisite

Download and install the latest available version of Docker Compose https://docs.docker.com/compose/install/

## Clone repository and start docker containers


```sh
git clone git@github.com:yannickscharf/real-time-analytics.git
cd real-time-analytics
```

Build and start the services using Docker Compose:

```sh
docker-compose up
docker-compose up -d (for detached mode)
```

## Mapped Ports

The services run on the following ports:
```
Host	   Container        Service

3000		3000        grafana
5432		5432        postgres
8080		8080        adminer
```

## Adminer

Open Adminer to view the database:

Navigate to `http://localhost:8080`. Connect to the database with the following credentials:

```sh
System: PostgreSQL
Server: postgres
Username: postgres
Password: example
```

## Grafana

Open Grafana to visualize the data:

Navigate to `http://localhost:3000`. Log in with the following credentials:

```sh
Username: grafana
Password: grafana
```

In order to add a new datasource open the sidebar menu in Grafana.
Select Connections and click on Datasources.
Add a new datasource and select PostgreSQL in the List.
Enter the following credentials:

```sh
Host URL: postgres:5432
Database name: postgres
Username: postgres
Password: example
TLS/SSL Mode: disable
```

## Ending the Service

To stop the containers without removing them:

```sh
docker-compose stop
```

Or to stop and remove the Docker containers, run:

```sh
docker-compose down
```
