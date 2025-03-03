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

    time.sleep(random.randint(1, 3)*(1+math.sin((seconds * 2.0 * math.pi) / 86400.0)))


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
