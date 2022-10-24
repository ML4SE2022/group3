from operator import attrgetter

sorted(student_objects, key=attrgetter('grade', 'age'))