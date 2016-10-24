dhclient h3-eth1
echo 1 > /proc/sys/net/ipv4/ip_forward
iptables -t nat -A POSTROUTING -o h3-eth1 -j MASQUERADE