#!/usr/bin/env python
import requests
import re
import boto3

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
amazon_ips = [item['ip_prefix'] for item in ip_ranges if item["service"] == "CLOUDFRONT" and item["region"] == "GLOBAL"]

for ip in amazon_ips: print(str(ip))

