class MyClass:
    class_attribute = "Class Attribute"

    def __init__(self, attribute):
        self.instance_attribute = attribute

    def instance_method(self):
        print(f"Instance Method - Instance Attribute: {self.instance_attribute}, Class Attribute: {self.class_attribute}")

    @classmethod
    def class_method(cls):
        print(f"Class Method - Class Attribute: {cls.class_attribute}")

    @staticmethod
    def static_method(x, y):
        return x + y

obj = MyClass("1")

obj.instance_method()

MyClass.class_method()

print(MyClass.static_method(3, 5))
