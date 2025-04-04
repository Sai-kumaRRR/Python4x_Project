# multiple  type of inheritance
# such as single
# multiple and
# multilevel inheritance.


class A:

    def method(self):
        return "method A"

    class B(A):  # Sai
        def method(self):
            return "method B"

    class C(A):  # sonu
        def method(self):
            return "method C"

        class D(B, C):  # sister # multiple , multilevel ,MRO (method resolution order)

            def method(self):
                return "method D"

            d = D()
            print(d.methodA())
            print(d.methodB())
            print(d.methodC())
            print(d.methodD())
