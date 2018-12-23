#!/usr/bin/env python
import requests

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']

#Amazon Connect needs access to AMAZON_CONNECT, EC2, and CLOUDFRONT over port 443
connect_ips = [item['ip_prefix'] for item in ip_ranges if (item["service"] == "AMAZON_CONNECT") and (item["region"] == "us-east-1")]
ec2_ips = [item['ip_prefix'] for item in ip_ranges if (item["service"] == "EC2") and (item["region"] == "us-east-1")]
cloudfront_ips = [item['ip_prefix'] for item in ip_ranges if (item["service"] == "CLOUDFRONT") and (item["region"] == "us-east-1")]
connect_ranges = []

for ip in connect_ips:
    connect_ranges.append(ip)
for ip in ec2_ips:
    connect_ranges.append(ip)
for ip in cloudfront_ips:
    connect_ranges.append(ip)

print("ranges needing access to tcp/443:")
for ip in connect_ranges: print(str(ip))
