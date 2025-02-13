# Wazuh and OpenVAS in Docker

To bring up on Windows using Docker Desktop,
```
docker compose up
```

On Linux,
```
docker-compose up
```

And then,

* Wazuh https://127.0.0.1:443/
* OpenVAS http://127.0.0.1:9392/

## Memory pages

Wazuh is very hungry for memory pages and will use more than are available by
default. Your Docker host probably needs configuring.

Instructions for Linux,
https://documentation.wazuh.com/current/deployment-options/docker/docker-installation.html#increase-max-map-count-on-your-host-linux

Instructions for Windows,
https://stackoverflow.com/a/69522855

## Documentation

https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html
We have a "single node" deployment.

https://greenbone.github.io/docs/latest/22.4/container/index.html


