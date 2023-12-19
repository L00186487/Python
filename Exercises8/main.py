from devices import Firewall
from devices import Switch
from devices import Loadbalancers

# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()

# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a switch instance
switch29 = Switch("switch29")
# Configure it
switch29.configure_switch()

# Create a Load Balancer instance
loadbalancer30 = Loadbalancers("Load Balancers 30")
# Configure it
loadbalancer30.configure_switch()