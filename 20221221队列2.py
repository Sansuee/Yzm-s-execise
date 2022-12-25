class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [0 for _ in range(k)] #建造空队列
        self.rear = 0 #队尾指针
        self.front = 0 #队首指针
        self.size = k 

    def enQueue(self, value: int) -> bool:
        self.rear=(self.rear+1) % self.size
        self.queue[self.rear]=value
        if self.rear==value:
            return True
        else:
            return False

    def deQueue(self) -> bool:
        t=self.front
        self.front=(self.front+1) % self.size
        return self.queue[self.front]
        if t==self.front:
            return True
        else:
            return False

    def Front(self) -> int:
        return self.front if not self.isEmpty else -1

    def Rear(self) -> int:
        return self.rear if not self.isEmpty else -1

    def isEmpty(self) -> bool:
        if self.front == self.rear:
            return True
            print("The Queue is empty")
        else:
            return False
            print("The Queue is not empty")
    
    def isFull(self) -> bool:
        if self.front == (self.rear+1) % self.size:
            return True
        else:
            return False

obj = MyCircularQueue(5)
param_1 = obj.enQueue(4)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()



