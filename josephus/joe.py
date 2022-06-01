#!/usr/bin/env python3.9

"""System module."""
import sys
from josephus import josephus

n = int(sys.argv[1])
josephus(n)
