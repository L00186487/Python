'''
Created By: Michael Floyd
Date: 24Nov23
Exercise: Demo For Loops

'''



# iterate through this dictionary below
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}

# For Loop
for ip_address in scan:
    port = scan[ip_address]
    print(f"IP Address: {ip_address}, Port: {port}")

# Use scan.items() for iteration instead
for ip_address, port in scan.items():
    print(f"IP Address: {ip_address}, Port: {port}")

# TUPLE - address each item in the tuple
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
    print(f"Found a service on {ipv4} at {port}")