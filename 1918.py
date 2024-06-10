#!/usr/bin/env python3
# Generate a random RFC1918 address
# GPL-2.0
# Authors: kellertk <tom@tompkel.net>
#          pdoroff <phil21@phil21.net>
import random
import ipaddress

# Define RFC1918 private IP address ranges
prefix_list = [
    '10.0.0.0/8',
    '192.168.0.0/16',
    '172.16.0.0/12',
]

def ip2n(ip):
    """Convert IP address to numeric value."""
    return int(ipaddress.ip_address(ip))

def n2ip(n):
    """Convert numeric value to IP address."""
    return str(ipaddress.ip_address(n))

def rndip(start, end):
    """Generate a random number within a specified range."""
    return random.randint(start, end)

# Iterate over each prefix
for prefix in prefix_list:
    network = ipaddress.ip_network(prefix)
    start_ip = ip2n(network.network_address)
    end_ip = ip2n(network.broadcast_address)
    
    # Calculate the range for /24 subnets
    start_subnet = start_ip >> 8
    end_subnet = end_ip >> 8
    
    # Generate a random /24 subnet within the range
    random_subnet_base = rndip(start_subnet, end_subnet) << 8
    random_subnet = ipaddress.ip_network(f"{n2ip(random_subnet_base)}/24")
    
    print(random_subnet)
