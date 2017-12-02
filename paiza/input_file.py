#! /usr/bin/env python
# -*- coding: utf-8 -*-

input_lines = int(input())
for i in range(input_lines):
    s = input().rstrip().split(',')
    print("hello = "+s[0]+" , world = "+s[1])
