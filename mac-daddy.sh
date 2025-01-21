#!/bin/bash

# Function to display usage instructions
usage() {
    echo "Usage: $0 -i <interface> -m <new-mac-address>"
    echo "Example: $0 -i eth0 -m 00:11:22:33:44:55"
    exit 1
}

# Function to validate MAC address format
validate_mac() {
    local mac=$1
    if [[ $mac =~ ^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$ ]]; then
        return 0
    else
        echo "Error: Invalid MAC address format."
        exit 1
    fi
}

# Check if the script is run as root
if [[ $EUID -ne 0 ]]; then
    echo "Error: This script must be run as root."
    exit 1
fi

# Parse command-line arguments
while getopts "i:m:" opt; do
    case $opt in
        i) interface=$OPTARG ;;
        m) new_mac=$OPTARG ;;
        *) usage ;;
    esac
done

# Ensure both arguments are provided
if [[ -z $interface || -z $new_mac ]]; then
    usage
fi

# Validate the MAC address
validate_mac $new_mac

# Check if the network interface exists
if ! ip link show $interface &> /dev/null; then
    echo "Error: Network interface $interface does not exist."
    exit 1
fi

# Bring the network interface down
echo "Bringing down the interface $interface..."
if ! ip link set dev $interface down; then
    echo "Error: Failed to bring down the interface $interface."
    exit 1
fi

# Change the MAC address
echo "Changing MAC address of $interface to $new_mac..."
if ! ip link set dev $interface address $new_mac; then
    echo "Error: Failed to change the MAC address."
    exit 1
fi

# Bring the network interface back up
echo "Bringing up the interface $interface..."
if ! ip link set dev $interface up; then
    echo "Error: Failed to bring up the interface $interface."
    exit 1
fi

echo "Successfully changed MAC address of $interface to $new_mac."
exit 0

