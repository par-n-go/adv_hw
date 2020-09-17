class MyFileWrite():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.f = open(self.filename, self.mode)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

    def write_file(self, value):
        self.f.write(value)

    def read_file(self):
        result = self.f.read()
        return result

with MyFileWrite('test.txt', 'r') as myfile:
    print (myfile.read_file())
