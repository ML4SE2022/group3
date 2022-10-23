import os

def convert_line_endings(file, in_encoding, out_encoding):
    # Convert line endings in input file to Windows
    content = ''
    outsize = 0
    with open(file, 'rb') as infile:
        content = infile.read()
        outsize = len(content)
        content = content.replace(b'\r\n', b'\n')
        content = content.replace(b'\r', b'\n')
        content = content.replace(b'\n', b'\r\n')
    with open(file, 'wb') as output:
        for line in content.splitlines(True):
            outsize += len(line) - 1
            output.write(line)
    print("Done. Saved %s bytes." % (len(content)-outsize))

convert_line_endings('file.txt', 'utf-8', 'utf-8')