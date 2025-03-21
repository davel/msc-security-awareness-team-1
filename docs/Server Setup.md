# Security Automation – Setting up servers for scanning

As part of the project that have been assigned to us we were required to have a Game Servers that shows different  logs and attacks against them,
so when scanned with Wazuh and Greenbone.

The steps that have been taken to create the servers are as follow:
* Creating a Python code that generates logs of attacks against the server and player activities.
* Copying the code on all server machines and executing it to run after the servers are powered on.
* Assigning the IP addresses for each server

Creating the Python code – the code that have been created have two main parts:
1.	To generate Players activities on the servers and store them in the log file 
2.	To generate the Attacks against the servers and also store them in the log file

Player activities – the following are list of the activities that the code generates in the log files of the server once they are powered on:
* Log messages
* Random player ID’s
* Player action
* Player joining and leaving
* Interaction with the NPC’s such as talking, trading, receiving quests and fighting NPC
* Collecting items
* Scoring points
* Simulate game events which are based on NPS interaction and players

Attacks – the attacks that will be simulated in the servers are as follow and the outcome from them will be used in the scans which will
be performed on Wazuh and Greenbone:
* Brute force
* SQL injection
* XSS (Cross-scripting) 
* Remote code execution
* Buffer overflow
* Privilege escalation
* Denial of Service (DoS)

The code is as follows,

```python
# Import necessary libraries
import time
import random
import datetime
import threading
import subprocess
import math

game_server_proc = subprocess.Popen(
    ["logger", "-t", "game_server"], stdin=subprocess.PIPE, text=True, bufsize=0
)

server_attack_proc = subprocess.Popen(
    ["logger", "-t", "server_attack"], stdin=subprocess.PIPE, text=True, bufsize=0
)

security_report_proc = subprocess.Popen(
    ["logger", "-t", "security_report"], stdin=subprocess.PIPE, text=True, bufsize=0
)


# Function to log messages
def log_event(message):
    security_report_proc.stdin.write(f"{message}\n")


# Function to append vulnerability reports
def report_vulnerability(message):
    server_attack_proc.stdin.write(f"{message}\n")


# Function to generate a random player ID
def generate_player_id():
    return random.randint(1000, 9999)


# Function to log player action
def log_player_action(player_id, action):
    game_server_proc.stdin.write(f"Player {player_id} performed action: {action}\n")


# Function to simulate a player joining
def simulate_player_join():
    player_id = generate_player_id()
    game_server_proc.stdin.write(f"Player {player_id} joined the game.\n")


# Function to simulate a player leaving
def simulate_player_leave():
    player_id = generate_player_id()
    game_server_proc.stdin.write(f"Player {player_id} left the game.\n")


# Function to simulate NPC interactions
def simulate_npc_interaction():
    actions = [
        "talking to an NPC",
        "trading with an NPC",
        "receiving a quest",
        "fighting an NPC",
    ]
    player_id = generate_player_id()
    action = random.choice(actions)
    game_server_proc.stdin.write(f"[NPC] Player {player_id} is {action}.\n")


# Function to simulate item collection
def simulate_item_collection():
    items = ["sword", "shield", "potion", "gem"]
    player_id = generate_player_id()
    item = random.choice(items)
    game_server_proc.stdin.write(f"[ITEM] Player {player_id} collected a {item}.\n")


# Function to simulate scoring points
def simulate_scoring_points():
    player_id = generate_player_id()
    points = random.randint(0, 100)
    game_server_proc.stdin.write(
        f"[SCORE] Player {player_id} scored {points} points.\n"
    )


# Function to simulate brute force attack
def simulate_brute_force_attack():
    attacker_id = f"Attacker_{random.randint(0, 999)}"
    log_event(f"{attacker_id} is attempting a brute-force attack on the login.")
    for i in range(1, 21):
        log_event(f"{attacker_id} failed login attempt #{i}.")
        time.sleep(0.5)


# Function to simulate SQL Injection attack
def simulate_sql_injection():
    log_event("Simulating SQL Injection attack.")
    report_vulnerability("SQL Injection attempt detected. Check input validation.")


# Function to simulate XSS attack
def simulate_xss_attack():
    log_event("Simulating XSS attack.")
    report_vulnerability("XSS vulnerability detected. Ensure proper sanitization.")


# Function to simulate Remote Code Execution (RCE)
def simulate_rce():
    log_event("Simulating Remote Code Execution (RCE).")
    report_vulnerability("System is vulnerable to RCE if remote execution is possible.")


# Function to simulate Buffer Overflow attack
def simulate_buffer_overflow():
    log_event("Simulating Buffer Overflow attack.")
    report_vulnerability(
        "Potential buffer overflow detected. Check memory safety mechanisms."
    )


# Function to simulate Privilege Escalation
def simulate_privilege_escalation():
    log_event("Simulating Privilege Escalation attempt.")
    report_vulnerability("Privilege escalation possible! Check sudo permissions.")


# Function to simulate Denial-of-Service (DoS) attack
def simulate_dos_attack():
    log_event("Simulating Denial-of-Service (DoS) attack.")
    for i in range(1, 21):
        log_event(f"Sending fake request #{i} to overload server...")
        time.sleep(0.2)
    report_vulnerability(
        "Potential DoS attack detected. Check for rate-limiting defenses."
    )


# Function to generate security report
def generate_security_report():
    log_event("Generating security report.")

    security_report_proc.stdin.write(
        f"\n========== SECURITY REPORT ==========\nGenerated on: {datetime.datetime.now()}\n=====================================\n"
    )


# Function to simulate random game events
def simulate_game_event():
    events = [
        "shoot",
        "move",
        "chat",
        "npc_interaction",
        "collect_item",
        "score_points",
    ]
    action = random.choice(events)
    if action == "npc_interaction":
        simulate_npc_interaction()
    elif action == "collect_item":
        simulate_item_collection()
    elif action == "score_points":
        simulate_scoring_points()
    else:
        player_id = generate_player_id()
        game_server_proc.stdin.write(
            f"[ACTION] Player {player_id} performed {action}.\n"
        )


# Function to simulate random player actions
def simulate_random_player_action():
    actions = [
        simulate_player_join,
        simulate_player_leave,
        simulate_game_event,
        simulate_brute_force_attack,
        simulate_sql_injection,
        simulate_xss_attack,
    ]
    random.choice(actions)()

    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (now - midnight).seconds

    time.sleep(
        random.randint(1, 3) * (1 + math.sin((seconds * 2.0 * math.pi) / 86400.0))
    )


# Function to simulate multiple players
def simulate_multiple_players():
    while True:
        simulate_random_player_action()


# Function to simulate periodic attacks
def simulate_attacks():
    counter = 0
    attack_functions = [
        simulate_rce,
        simulate_buffer_overflow,
        simulate_privilege_escalation,
        simulate_brute_force_attack,
        simulate_sql_injection,
        simulate_xss_attack,
        simulate_dos_attack,
    ]
    while True:
        random.choice(attack_functions)()
        counter += 1
        if counter % 10 == 0:
            generate_security_report()
        time.sleep(random.randint(1, 5))


# Start game simulation and attack simulation in parallel threads
game_thread = threading.Thread(target=simulate_multiple_players, daemon=True)
attack_thread = threading.Thread(target=simulate_attacks, daemon=True)

game_thread.start()
attack_thread.start()

# These joins should never return!
game_thread.join()
attack_thread.join()
```

Once the code was built and saved as .py file, then it was transferred to the servers.
To transfer the file on the server the following commands have been used for secure transfer from Ubuntu Desktop machine as the .py code was build
in a desktop environment:
*  `sftp student@192.168.123.30` - that was the IP of the server at the time. 
* `put game_server_simulator.py`
* `exit`

When the transfer was completed using “ssh” I connect to the server to complete the next steps and enable the code to start working when the server is powered on.
To connect to it the following command was used
* `ssh student@192.168.123.30`

When I was connected to the server the next thing that have been done was to check if the python is installed as it was required for the .py code to run.
* python3 -version`

The above command displays if the python3 which was installed. In my case python3 was not installed so it had to be install it on the server.
To install it the following commands have been used to obtain it on the server:
* `sudo apt update`
* `sudo apt install python3`
* `sudo apt install python3-pip`

Once the python3 was successfully installed the next what have been done was to change the permissions of the .py file, so it can be executable.
To do that I have used the following:
* `chmod +x game_server_simulator.py`

When the permissions of the file have been changed so it can be executed on the server the following steps have to been taken
in order to make it run automatically when the server starts. The first step was to open the system configuration file.
To do that the following command have been used:
* `sudo nano /etc/systemd/system/game_server.service`

The following picture represents the configuration that have been made in order the script to start running
and creating log entries once the server is up and running. 
![image](./Images/Automatic Start.png)

Once that have been included in the configuration file the next step was to enable and start the service. To do that the following commands have been used:
* `sudo systemctl daemon-reload` – to reload the configuration
* `sudo systemctl enable game_server` – to enable the script
* `sudo systemctl start game_server` – to start it
* `sudo systemctl status game_server` – to check if the script is running properly
![image](Images/Status.png)

The next thing that have been done was to create two more servers like that.
As we are using virtual environment I was able to clone it so we have ended up with three server.
In a real case scenario the same steps will have to be performed for each individual server.

Once I had all three of them the next thing was to assign them the proper IP addresses as if they all had the same IP simply they won’t work
as it will create interference. First what I did was to add second network card in each of them.
The first card was left on NAT so the servers can get network access and the second one was set to Bridged adapter so it can communicate with the Wazuh
and Greenbone scanners. 

To change the IP addresses on the servers the following steps have been taken:
1.	Locate the netplan of the server – to do that the following command have been used:
 * `ls /etc/netplan/`
2.	To change the netplan and set static IP on each server:
 * `sudo nano /etc/netplan/"name of the netplan that have been given"
3.	The following picture will show my configuration of the netplan and the setup of the IP address
 * ![image](Images/Netplan.png)

4.	Once the netplan have been edited according to my needs I have save it and to implement the changes fully the following command have been used:
 * `sudo netplan apply`

By doing this steps on each server individually I have successfully changed the IP addresses and they were ready for the Wazuh agent to be installed on them.
Wazuh agent is needed on each individual machine so the Manager can retrieve data from them. To be able to install the agent the following command 
was executed on each server:

```$ wget https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.10.1-1_amd64.deb && sudo WAZUH_MANAGER='192.168.112.2'
WAZUH_AGENT_NAME='name on the server that will be monitored' dpkg -i ./wazuh-agent_4.10.1-1_amd64.deb
```

By doing so, and adding the name of the server that have to be monitored after the equal sign which is right after WAZUH_AGENT_NAME the manager
was able to detect that server and is able to perform scans on it. This step was to repeat it on each server and all three of them become visible on the
dashboard of Wazuh.
