#!/bin/bash
jq -r '[.prefixes[] | select(.region=="us-east-1").ip_prefix] | .[]' < ip-ranges.json |wc -l
jq -r '[.prefixes[] | select(.region=="us-east-1").ip_prefix] - [.prefixes[] | select(.service=="EC2").ip_prefix] | .[]' < ip-ranges.json |wc -l
jq -r '[.prefixes[] | select(.region=="us-east-1" and .service=="AMAZON").ip_prefix] - [.prefixes[] | select(.region=="us-east-1" and .service=="EC2").ip_prefix] | .[]' < ip-ranges.json |wc -l
jq -r '[.prefixes[] | select(.region=="us-east-1" and .service=="AMAZON_CONNECT").ip_prefix] - [.prefixes[] | select(.region=="us-east-1" and .service=="EC2").ip_prefix] | .[]' < ip-ranges.json |wc -l
