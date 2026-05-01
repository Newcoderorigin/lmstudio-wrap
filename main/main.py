import subprocess
import sys
import os

# Start the server in the background
server_proc = subprocess.Popen([sys.executable, os.path.join(os.path.dirname(__file__), 'server.py')])

try:
    # Start the GUI (waits until closed)
    subprocess.run([sys.executable, os.path.join('gui', 'app.py')])
finally:
    # Clean up: terminate the server when GUI closes
    server_proc.terminate()
    server_proc.wait()
