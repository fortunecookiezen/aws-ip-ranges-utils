#!/usr/bin/env python
import requests

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
amazon_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "S3" and item["region"] == "us-east-1"]

amazon_s3=[]

for ip in amazon_ips:
    amazon_s3.append(ip)

for ip in amazon_s3: print(str(ip))
