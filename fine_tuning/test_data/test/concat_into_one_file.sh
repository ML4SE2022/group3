for f in *.py; do (cat "${f}"; echo) >> test.py; done
for f in *.java; do (cat "${f}"; echo) >> test.java; done