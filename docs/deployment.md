# Deployment of the monitoring system

## Goals

Installation of **OpenVAS** and **Wazuh** in a reproducible and maintainable manner.

The initial requirement was for Nessus rather than OpenVAS. However, its
licensing system was awkward to work with while we were prototyping the build.
OpenVAS meets our requirements and has no such installation problems, so
the requirement was changed.

OpenVAS is distributed as a component within
[Greenbone Vulnerability Management](https://greenbone.github.io/docs/latest/).

## Deployment host

The final system was deployed as a VirtualBox VM. It was configured as follows,

* OS: Ubuntu 24.04
* RAM: 4Gb
* Swap: 24Gb
* 3×NICs
  * NAT
  * Bridged, DHCP
  * Bridged, 192.168.112.2/24
* Tailscale VPN

## Docker

We decided to use [Docker](https://www.docker.com/) to deploy our monitoring
system. Compared to a build on a virtual machine running a conventional full
operating system (such as Ubuntu), Docker gives us some advantages for
collaboration. The build configuration can be kept in Git and can easily be
re-run.

Wazuh and Greenbone both contain multiple services, which when deployed
through Docker require multiple Docker VMs. To automate the process of
configuring the VMs they both provide `docker-compose.yml` configuration files.
`[docker-compose](https://docs.docker.com/compose/)` is a technology built on
top of Docker that allows a system built from multiple Docker VMs to be
assembled automatically from a configuration file.

We will use the provided `docker-compose` file as this is the installation
method documented by both Wazuh and Greenbone.

### Configuring the host

The Docker configuration works under both Linux and Windows. For the final
deployment we have used Linux.

#### Running under Windows

For development, we could run the system under Windows using Docker.

One of the applications contained within Wazuh is
[OpenSearch](https://opensearch.org/). This requires an exceptionally large
number of memory mappings. On Docker Windows, which uses WSL2, this will exceed
[operating system kernel's limit](https://docs.kernel.org/admin-guide/sysctl/vm.html#max-map-count).

To resolve this, a sysctl parameter can be changed in WSL2. A `.wslconfig` file
can be placed in the user's home directory with the follow contents,
```
[wsl2] 
kernelCommandLine = sysctl.vm.max_map_count=262144
```
This is described in more detail here,
https://stackoverflow.com/a/71121306

After updating Docker Desktop we hit a second problem in which it cannot
start VMs. This was resolved by updating WSL2 as well, with the Windows command
`wsl --update --web-download`. This described here,
https://superuser.com/a/1875865

#### Running under Linux

Ubuntu 24.04 was used for the final installation. It was installed from the
"server" ISO. When prompted by the installer, the "docker" Snap was installed.
No sysctl configuration was needed, the default `max_map_count` was already
higher than required.

We set up the user account `team1`.

After installation, some configuration is required to allow Docker to be used
by non-root users. This is preferable on the principle of granting a process
the smallest set of permissions required.

```
sudo addgroup --system docker
sudo adduser team1 docker
newgrp docker
```

This is described in the documentation here,
https://github.com/canonical/docker-snap?tab=readme-ov-file#running-docker-as-normal-user

## Building the service

In the Git repository there is a `docker-compose.yml` file at the root
which pulls in both Wazuh and Greenbone. Their reference configuration
has also been committed to Git.

https://github.com/davel/msc-security-awareness-team-1/

### Wazuh

Wazuh [documents](https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html)
single and multi node deployments. We have opted for single node deployment.

Wazuh requires certificates to be created. Self-signed certificates were
created and added to the Git repository.

## Starting the service

The service does not start automatically on boot.

1. Log on via ssh.
2. If necessary, clone the repository from GitHub. `git clone https://github.com/davel/msc-security-awareness-team-1/`
3. Join the [screen](https://www.gnu.org/software/screen/manual/screen.html) session with `screen -r`. (Or create one with just `screen`).
4. cd `msc-security-awareness-team-1`
5. `docker-compose up`
