#!/bin/sh
ip link set PC1-eth0
ip addr add 10.10.14.1/24 dev PC1-eth0
ip addr del 10.0.0.1/8 dev PC1-eth0
ip -6 addr add fd24:ec43:12ca:c001:14::1/80 dev PC1-eth0

ip route add default via 10.10.14.4
ip -6 route add default via fd24:ec43:12ca:c001:14::4