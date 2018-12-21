#!/usr/bin/env python
import requests

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
connect_ips = [item['ip_prefix'] for item in ip_ranges if (item["service"] == "AMAZON_CONNECT") and (item["region"] == "us-east-1")]
ec2_ips = [item['ip_prefix'] for item in ip_ranges if (item["service"] == "EC2") and (item["region"] == "us-east-1")]
cloudfront_ips = [item['ip_prefix'] for item in ip_ranges if (item["service"] == "CLOUDFRONT") and (item["region"] == "us-east-1")]
print("ranges needing access to tcp/443:")
for ip in connect_ips: print(str(ip))
for ip in ec2_ips: print(str(ip))
for ip in cloudfront_ips: print(str(ip))
