#!/bin/sh
ip link set PC2-eth0
ip addr add 10.10.24.2/24 dev PC2-eth0
ip addr del 10.0.0.2/8 dev PC2-eth0
ip -6 addr add fd24:ec43:12ca:c001:24::2/80 dev PC2-eth0

ip route add default via 10.10.24.4
ip -6 route add default via fd24:ec43:12ca:c001:24::4