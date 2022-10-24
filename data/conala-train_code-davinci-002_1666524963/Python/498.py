import sys

def replace_char(filename, old_char, new_char):
    with open(filename, 'r') as f:
        text = f.read()
    text = text.replace(old_char, new_char)
    with open(filename, 'w') as f:
        f.write(text)

if __name__ == '__main__':
    replace_char(sys.argv[1], sys.argv[2], sys.argv[3])