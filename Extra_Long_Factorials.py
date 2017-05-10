#!/bin/python3

import sys

product =1
n = int(input().strip())
for i in range (1,n+1):
    product = product * i
print (product)