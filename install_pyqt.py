import subprocess
import os
import sys

try:
    # Try to import PyQt5
    from PyQt5.QtWidgets import QApplication
except ImportError:
    print("PyQt5 is not installed. Attempting to install...")
    subprocess.run(["pip", "install", "PyQt5"])
    
    # Add the PyQt5 DLLs to the PATH
    install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".venv", "Lib", "site-packages", "PyQt5", "Qt", "bin"))
    os.environ['PATH'] = f"{install_path};{os.environ['PATH']}"
    
    print("PyQt5 installed successfully. Restarting the script...")
    
    # Restart the script
    python_path = sys.executable
    script_path = os.path.join(os.path.dirname(__file__), "banner.pyw")
    subprocess.run([python_path, script_path])
    sys.exit(0)  # Exit the current instance
