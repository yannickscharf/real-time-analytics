# real-time-analytics

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd real-time-analytics
   ```

2. Build and start the services using Docker Compose:

   ```sh
   docker-compose up
   ```

   Or to run in detached mode:

   ```sh
   docker-compose up -d
   ```

3. Open Adminer to view the database:

   - Navigate to `http://localhost:8080`
   - Connect to the database with the following credentials:
     - **System**: PostgreSQL
     - **Server**: postgres (service name defined in [docker-compose.yml](http://_vscodecontentref_/1))
     - **Username**: postgres (default PostgreSQL superuser)
     - **Password**: example (defined in [docker-compose.yml](http://_vscodecontentref_/2))

4. Open Grafana to visualize the data:
   - Navigate to `http://localhost:3000`
   - Log in with the following credentials:
     - **Username**: grafana
     - **Password**: grafana

## Ending the Service

To stop and remove the Docker containers, run:

```sh
docker-compose down
```

Or to stop the containers without removing them:

```sh
docker-compose stop
```
