from threading import Thread, Semaphore


class Printer():
    consume = Semaphore(0)
    produce = Semaphore(1)
    item =  0

    def printData(self):
        self.consume.acquire()
        print('Consumed : ', self.item)
        self.produce.release()

    def setData(self,item):
        self.produce.acquire()
        self.item = item
        print('Produced : ', self.item)
        self.consume.release()


class Producer(Thread):
    def __init__(self,printer):
        super().__init__()
        self.printer = printer

    def run(self):
        for i in range(20):
            self.printer.setData(i)


class Consumer(Thread):
    def __init__(self,printer):
        super().__init__()
        self.printer = printer

    def run(self):
        for i in range(20):
            self.printer.printData()


printer = Printer()
consumer = Consumer(printer)
producer = Producer(printer)
consumer.start()
producer.start()

