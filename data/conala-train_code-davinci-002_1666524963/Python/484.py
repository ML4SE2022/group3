class Base(object):
    def __init__(self):
        print "Base created"

class ChildA(Base):
    def __init__(self):
        Base.__init__(self)
        print "ChildA created"

class ChildB(Base):
    def __init__(self):
        super(ChildB, self).__init__()
        print "ChildB created"

ChildA()
ChildB()