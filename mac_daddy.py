# Used to parse command line arguments.
import argparse
# Used to check format of MAC address.
import re
# Used for commands outside of Python.
import subprocess
# Used for exit codes determining success or failure.
import sys

def usage():
    """Print usage information and exit."""
    print("Usage: script.py -i <interface> -m <new-mac-address>")
    print("Example: script.py -i eth0 -m 00:11:22:33:44:55")
    sys.exit(1)

def validate_mac(mac):
    """Validate the MAC address format."""
    if re.match(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$", mac):
        return True
    print("Error: Invalid MAC address format.")
    sys.exit(1)

def check_root():
    """Check if the script is run as root."""
    
    if not (subprocess.geteuid() == 0):
        print("Error: This script must be run as root.")
        sys.exit(1)

def interface_exists(interface):
    """Check if the network interface exists."""

    result = subprocess.run(["ip", "link", "show", interface], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def change_mac(interface, new_mac):
    """Change the MAC address of the specified interface."""
    
    print(f"Bringing down the interface {interface}...")
    
    if subprocess.run(["ip", "link", "set", "dev", interface, "down"]).returncode != 0:
        print(f"Error: Failed to bring down the interface {interface}.")
        sys.exit(1)

    print(f"Changing MAC address of {interface} to {new_mac}...")
    
    if subprocess.run(["ip", "link", "set", "dev", interface, "address", new_mac]).returncode != 0:
        print("Error: Failed to change the MAC address.")
        sys.exit(1)

    print(f"Bringing up the interface {interface}...")
    
    if subprocess.run(["ip", "link", "set", "dev", interface, "up"]).returncode != 0:
        print(f"Error: Failed to bring up the interface {interface}.")
        sys.exit(1)

    # Verify the change in MAC address.
    print(f"Successfully changed MAC address of {interface} to {new_mac}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Change MAC Address")
    parser.add_argument("-i", "--interface", required=True, help="Network interface")
    parser.add_argument("-m", "--mac", required=True, help="New MAC address")
    args = parser.parse_args()

    # Checks if the script is run as root.
    check_root()
    # Validates the MAC address format.
    validate_mac(args.mac)
    
    if not interface_exists(args.interface):
        print(f"Error: Network interface {args.interface} does not exist.")
        sys.exit(1)

    change_mac(args.interface, args.mac)
