import random;


class agent(object):
    def __init__(self,env):
        self.env=env;

    def go(self,n):
        raise NotImplementedError("go");

