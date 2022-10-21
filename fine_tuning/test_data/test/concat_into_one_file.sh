for f in *converted.py; do (cat "${f}"; echo) >> test.py; done
for f in *converted.java; do (cat "${f}"; echo) >> test.java; done