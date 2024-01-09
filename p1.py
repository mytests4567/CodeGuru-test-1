print("Hello World")

def read_file_noncompliant(filename):
    def foo(filename):
        return open(filename, 'r')
    file = foo(filename)
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()
