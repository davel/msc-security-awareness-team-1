# Wazuh agent

Wazuh requires a program, the agent, to run on every system that it is
monitoring to allow it to capture data.

Change `XXX` to be the name of the server being monitored, as displayed in
Wazuh.

```
$ wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.10.1-1_amd64.deb && sudo WAZUH_MANAGER='192.168.112.2' WAZUH_AGENT_NAME='XXX' dpkg -i ./wazuh-agent_4.10.1-1_amd64.deb 
```
