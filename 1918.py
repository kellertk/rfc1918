#!/usr/bin/env python3
# Generate a random RFC1918 /24 subnet
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

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

# Select a random prefix
random_prefix = random.choice(prefix_list)
network = ipaddress.ip_network(random_prefix)
start_ip = ip2n(network.network_address)
end_ip = ip2n(network.broadcast_address)

# Calculate the range for /24 subnets
start_subnet = start_ip >> 8
end_subnet = end_ip >> 8

# Generate a random /24 subnet within the range
random_subnet_base = rndip(start_subnet, end_subnet) << 8
random_subnet = ipaddress.ip_network(f"{n2ip(random_subnet_base)}/24")

print(random_subnet)
