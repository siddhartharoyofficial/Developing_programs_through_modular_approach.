#!/bin/bash

echo "CPU Load:"
top -bn1 | grep load | awk '{printf "%.2f\n", $(NF-2)}'
echo "Memory Usage:"
free | grep Mem | awk '{printf "used: %.2f MB\nfree: %.2f MB\n", ($3/1024), ($4/1024)}'
echo "Disk Usage:"
df -h | grep /dev/sda1 | awk '{printf "used: %s\nfree: %s\n", $3, $4}'
echo "Network Usage:"
iftop -t -s 1 -n | head -n 10
echo "Active Logged In Users:"
who
