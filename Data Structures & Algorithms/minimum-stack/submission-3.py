class MinStack:

    def __init__(self):
        self.skt = []
        self.min_skt = []

    def push(self, val: int) -> None:
        self.skt.append(val)

        if not self.min_skt:
            self.min_skt.append(val)
        
        elif val <= self.min_skt[-1]:
            self.min_skt.append(val)
       

    def pop(self) -> None:
        if self.skt[-1] == self.min_skt[-1]:
            self.min_skt.pop()
        self.skt.pop()

    def top(self) -> int:
        return self.skt[-1]

    def getMin(self) -> int:
        return self.min_skt[-1]
