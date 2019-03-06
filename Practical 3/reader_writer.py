from threading import Lock, Thread


class ReaderWriter:

    rw_lock = Lock()
    lock = Lock()
    read_count = 0

    def write(self, value):
        self.rw_lock.acquire()
        print('Writing :', value)
        self.rw_lock.release()

    def read(self,value):
        self.lock.acquire()
        self.read_count+=1
        if self.read_count is 1:
            self.rw_lock.acquire()
        self.lock.release()

        print('Reading :',value)

        self.lock.acquire()
        self.read_count-=1
        if self.read_count is 0:
            self.rw_lock.release()
        self.lock.release()

class Reader(Thread):
    def __init__(self,rw):
        super().__init__()
        self.rw = rw
    def run(self):
        for i in range(20):
            self.rw.read(i)

class Writer(Thread):
    def __init__(self,rw):
        super().__init__()
        self.rw = rw
    def run(self):
        for i in range(20):
            self.rw.write(i)

rw = ReaderWriter()
reader = Reader(rw)
writer = Writer(rw)
writer.start()
reader.start()
