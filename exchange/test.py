from dataclasses import dataclass


@dataclass
class A():
    a: int


a = A(1)
b = A(2)
print(a)
print(b)
l = [a, b]
print(l)
a.a = 5
print(a)
print(l)
