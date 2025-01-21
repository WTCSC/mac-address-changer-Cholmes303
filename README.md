# MAC Address Changer Script

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tp86o73G)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17743676)



This script allows you to change the MAC address of a specified network interface. It validates the provided MAC address, handles errors, and ensures the changes are applied safely.

## Features

- Accepts command-line arguments for the network interface and new MAC address.

- Validates MAC address format.

- Handles common errors (e.g., invalid interface, permission issues).

- Provides clear error messages and success confirmations.

## Installation Instructions

1. Download the Script:
Save the script file (./mac-daddy.sh) to your system.

2. Make the Script Executable:
Run the following command to grant execution permissions:

```
chmod +x mac-daddy.sh
```

3. Ensure Dependencies Are Installed:

 - The script relies on the ip command, which is typically included in most Linux distributions.

## Usage

To run the script, you must have administrative privileges. Use the following syntax:

```
sudo ./mac-daddy.sh -i <interface> -m <new-mac-address>
```

### Examples:

1. Change the MAC address of eth0 to 00:11:22:33:44:55:

```
sudo ./mac-daddy.sh -i eth0 -m 00:11:22:33:44:55
```

2. Change the MAC address of wlan0 to AA:BB:CC:DD:EE:FF:

```
sudo ./mac-daddy.sh -i wlan0 -m AA:BB:CC:DD:EE:FF
```

## Script Details
### Command-Line Arguments:

- -i: Specifies the network interface (e.g., eth0, wlan0).

- -m: Specifies the new MAC address (e.g., 00:11:22:33:44:55).

### Validation:

- Ensures the MAC address is in the correct format (XX:XX:XX:XX:XX:XX, where XX are hexadecimal values).

### Error Handling:

- Invalid MAC Address: Prints an error if the MAC address format is incorrect.

- Missing Interface: Checks if the specified network interface exists.

- Permission Denied: Ensures the script is run with root privileges.

- Failed Commands: Handles errors during network interface operations (e.g., bringing the interface down or up).

### Troubleshooting

1. Error: This script must be run as root

- Solution: Use sudo to run the script.

2. Error: Invalid MAC address format

- Solution: Verify the MAC address format is correct. Example: 00:11:22:33:44:55.

3. Error: Network interface does not exist

- Solution: Check the available interfaces using the command:

```
ip link
```

4. Error: Failed to bring the interface up or down

- Solution: Ensure the interface is not in use or locked by another process.

## Demonstration

Below is an example of the script in action:

```
$ sudo ./mac-daddy.sh -i eth0 -m 00:11:22:33:44:55
Bringing down the interface eth0...
Changing MAC address of eth0 to 00:11:22:33:44:55...
Bringing up the interface eth0...
Successfully changed MAC address of eth0 to 00:11:22:33:44:55.
```

## Notes

- Ensure you have the necessary permissions and dependencies installed before running the script.

- Use this script responsibly and ensure compliance with your network policies.

