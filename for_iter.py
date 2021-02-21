class For:
    def __init__(self,init,conditional,incrementor):
        self.val = init()
        self.conditional = conditional
        self.incrementor = incrementor
        self.first_loop = True
    def __iter__(self):
        return self
    def __next__(self):
        if not self.first_loop:
            self.val = self.incrementor(self.val)
        self.first_loop = False
        if not self.conditional(self.val):
            raise StopIteration
        return self.val
def std_init(val=0):
    return lambda: val
zero = std_init(0)
one = std_init(1)
def std_cond(val):
    return lambda i: i < val
def std_inc(amount=1):
    return lambda i: i+amount
