import socket
import databaseSIEM
from flask import Flask, render_template


# Database initialisation
databaseSIEM.db_initialization()

# Print period
databaseSIEM.db_period_print()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("0.0.0.0", 717))

print("NightWing en écoute...")

# Launch the server and receive the alert
while True:
    data, addr = sock.recvfrom(4096)
    log = data.decode('utf-8', errors='ignore').strip()

    databaseSIEM.db_write_raw(addr[0], log)
    print(f"[{addr[0]}] {log}")
    
    result_raw = databaseSIEM.db_read_raw()
    print(result_raw)

