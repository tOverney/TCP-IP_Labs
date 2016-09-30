#!/bin/sh
ip link set PC4-eth0
ip link set PC4-eth1
ip link set PC4-eth2

ip addr add 10.10.14.4/24 dev PC4-eth0;
ip -6 addr add fd24:ec43:12ca:c001:14::4 dev PC4-eth0

ip addr add 10.10.24.4/24 dev PC4-eth1
ip -6 addr add fd24:ec43:12ca:c001:24::4 dev PC4-eth0

ip addr add 10.10.34.4/24 dev PC4-eth2
ip -6 addr add fd24:ec43:12ca:c001:34::4 dev PC4-eth0


# Enable ip forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward
echo 1 > /proc/sys/net/ipv6/conf/all/forwarding