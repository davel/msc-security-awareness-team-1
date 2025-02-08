# Wazuh and Nessus in Docker

To bring up on Windows using Docker Desktop,
```
docker compose up
```

On Linux,
```
docker-compose up
```

## Memory pages

Wazuh is very hungry for memory pages and will use more than are available by
default. Your Docker host probably needs configuring.

Instructions for Linux,
https://documentation.wazuh.com/current/deployment-options/docker/docker-installation.html#increase-max-map-count-on-your-host-linux

Instructions for Windows,
https://stackoverflow.com/a/69522855
