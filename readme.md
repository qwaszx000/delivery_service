# delivery service

Use `db` instead of `127.0.0.1` to access database.
Because we use docker.

To start server use:
`sudo docker-compose up`
`sudo docker-compose up -d` - start and detach(run as daemon)
To access bash in running docker container:
`sudo docker exec -t -i <CONTAINER ID> bash`
Then `python3 manage.py migrate` to migrate

Result will be in `http://127.0.0.1:80/`
