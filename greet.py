import sys
from myHelloModule import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])