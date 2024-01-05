class Grandparent:
    def grandparent_method(self):
        return "Grandparents method"
class Parent(Grandparent):
    def parent_method(self):
        return "Parents method"
class child(Parent):
    def child_method(self):
        return "child method"
child = child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())
