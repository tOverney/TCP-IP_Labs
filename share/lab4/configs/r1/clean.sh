#!/bin/sh

# This script clear the logs
varpath='/home/lca2/Desktop/shared/lab4/configs/r1'

rm $varpath/logs/zebra.log
touch $varpath/logs/zebra.log
chmod 666 $varpath/logs/zebra.log

rm $varpath/logs/ripd.log
touch $varpath/logs/ripd.log
chmod 666 $varpath/logs/ripd.log

rm $varpath/logs/ripngd.log
touch $varpath/logs/ripngd.log
chmod 666 $varpath/logs/ripngd.log

/etc/init.d/quagga restart

