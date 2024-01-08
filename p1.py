def read_file_noncompliant(filename):
    file = open(filename, 'r')
    # Noncompliant: method returns without properly closing the file.
    return file.readlines()
