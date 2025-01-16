#!/bin/bash

case "$1" in
    ip_link)
        echo "MAC addresses for all interfaces:"
        ip link show | grep -oP '(?<=ether )([0-9a-f]{2}(:[0-9a-f]{2}){5})'
        ;;
    change)
        sudo ip link set dev enp0s3 address $(openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/:$//')
        echo "To see the new MAC address, use the command \"ip_link\""
        ;;
esac