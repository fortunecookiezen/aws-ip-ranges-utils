#!/usr/bin/env python
import requests
import sys
import getopt

service = input("Which Amazon service are you searching for: eg AMAZON_CONNECT?  ")
if not service:
    print("valid values: AMAZON | AMAZON_CONNECT | CLOUD9 | CLOUDFRONT | CODEBUILD | EC2 | ROUTE53 | ROUTE53_HEALTHCHECKS | S3")
    print('usage: service-ipranges.py $SERVICE $REGION, eg ./service-ipranges.py AMAZON_CONNECT us-east-1')
    sys.exit()


region = input("Which region are you looking for it in?  ")
if not region:
    print("Valid values: ap-northeast-1 | ap-northeast-2 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ca-central-1 | cn-north-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | sa-east-1 | us-east-1 | us-east-2 | us-gov-west-1 | us-west-1 | us-west-2 | GLOBAL")
    print('usage: service-ipranges.py $SERVICE $REGION, eg ./service-ipranges.py AMAZON_CONNECT us-east-1')
    sys.exit()

#    SERVICE
#    The subset of IP address ranges. Specify AMAZON to get all IP address ranges (for example, the ranges in the EC2 subset are also in the AMAZON subset). Note that some IP address ranges are only in the AMAZON subset.
#    Type: String Valid values: AMAZON | AMAZON_CONNECT | CLOUD9 | CLOUDFRONT | CODEBUILD | EC2 | ROUTE53 | ROUTE53_HEALTHCHECKS | S3
#    Example: "service": "AMAZON"

#    REGION
#    The AWS region or GLOBAL for edge locations. Note that the CLOUDFRONT and ROUTE53 ranges are GLOBAL.
#    Type: String Valid values: ap-northeast-1 | ap-northeast-2 | ap-south-1 | ap-southeast-1 | ap-southeast-2 | ca-central-1 | cn-north-1 | eu-central-1 | eu-west-1 | eu-west-2 | eu-west-3 | sa-east-1 | us-east-1 | us-east-2 | us-gov-west-1 | us-west-1 | us-west-2 | GLOBAL
#    Example: "region": "us-east-1"

ip_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
service_ips = [item['ip_prefix'] for item in ip_ranges if (item["service"] == service.upper()) and (item["region"] == region.lower())]

for ip in service_ips: print(str(ip))
