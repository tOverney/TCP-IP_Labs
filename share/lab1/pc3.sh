#!/bin/sh
ip link set PC3-eth0
ip addr add 10.10.34.3/24 dev PC3-eth0
ip addr del 10.0.0.3/8 dev PC3-eth0
ip -6 addr add fd24:ec43:12ca:c001:34::3/80 dev PC3-eth0

ip route add default via 10.10.24.4
ip -6 route add default via fd24:ec43:12ca:c001:24::4