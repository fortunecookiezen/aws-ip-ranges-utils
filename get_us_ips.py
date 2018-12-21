#!/usr/bin/env python
import requests
import re
import boto 

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
#amazon_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "AMAZON" and item["region"] == "us-east-1"]
amazon_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "AMAZON" and item["region"] == "us-east-1"]
connect_ips = [item['ip_prefix'] for item in ip_ranges if (item["service"] == "AMAZON_CONNECT") and (item["region"] == "us-east-1")]
ec2_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "EC2"]
amazon_ips_less_ec2=[]

for ip in amazon_ips:
    if ip not in ec2_ips:
        amazon_ips_less_ec2.append(ip)

for ip in connect_ips:
        if ip not in ec2_ips:
            amazon_ips_less_ec2.append(ip)

for ip in amazon_ips_less_ec2: print(str(ip))
