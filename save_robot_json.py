#! /usr/bin/env python3

from openravepy import *

env = Environment()

env.Load("robots/kawada-hironx.zae")
env.Save("kawada.json")
