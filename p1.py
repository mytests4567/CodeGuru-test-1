print("Hello World")

def read_file_noncompliant(filename):
    def oopen(fn):
        return open(filename, 'r')
    file = oopen(filename)
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()
