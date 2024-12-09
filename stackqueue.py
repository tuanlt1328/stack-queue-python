class stack:
    def __init__(self):
        self.data=[]
    def isEmpty(self) -> bool:
        return len(self.data)==0
    def size(self):
        return len(self.data)
    def push(self, val):
        self.data.append(val)
    def pop(self):
        if not self.isEmpty():
            s=self.data[len(self.data)-1]
            del self.data[len(self.data)-1]
            return s
        raise ValueError("There are nothing to pop")
    def first(self):
        return self.data[0]
    def last(self):
        return self.data[len(self.data)-1]

class queue:
    def __init__(self):
        self.data=[]
    def isEmpty(self) -> bool:
        return len(self.data)==0
    def size(self):
        return len(self.data)
    def enqueue(self, val):
        self.data.append(val)
    def dequeue(self):
        if not self.isEmpty():
            s=self.data[0]
            del self.data[0]
            return s
        raise ValueError("There are nothing to dequeue")
    def first(self):
        return self.data[0]
    def last(self):
        return self.data[len(self.data)-1]

