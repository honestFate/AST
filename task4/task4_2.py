from .task4 import Stack


def is_balanced(line):
    chars = Stack()
    for c in line:
        if c == '(':
            chars.push(c)
        if c == ')' and (chars.size() == 0 or chars.pop() != '('):
            return False
    return chars.size() == 0

def is_balanced_advanced(line):
    chars = Stack()
    pairs = {'(': ')', '{': '}', '[': ']'}
    openers = set(pairs)
    closers = set(pairs.values())

    for c in line:
        if c in openers:
            chars.push(c)
        elif c in closers and (chars.size() == 0 or pairs[chars.pop()] != c):
            return False
    return chars.size() == 0

def evaluate_postfix(expression):
    s1 = Stack()
    s2 = Stack()

    for token in reversed(expression.split()):
        s1.push(token)

    while s1.size() > 0:
        token = s1.pop()

        if token == '=':
            return s2.pop()

        if token == '+':
            b = s2.pop()
            a = s2.pop()
            s2.push(a + b)
        elif token == '*':
            b = s2.pop()
            a = s2.pop()
            s2.push(a * b)
        else:
            s2.push(int(token))

    return s2.peek()


"""
task: 4.1
name: size(), pop(), push() и peek()
pop O(1) амортизированно
push O(1) амортизированно


task: 4.3
name: как отработает цикл
while stack.size() > 0:
    print(stack.pop())
    print(stack.pop())
на пустом ничего не выведет
при чётном количестве элементов выведет все элементы списка
при нечетном на последней итерации выведет дополнительно None

task: 4.4
name: head of stack in the begining of the list
pop O(n)
push O(n)
всегда сдвигаем все элементы правее, что даёт O(n)

task: 4.5
name: balanced check
time: O(n)
memory: O(n)

task: 4.6
name: balanced check (three types)
time: O(n)
memory: O(n)
рефлексия: использовал словарь для сопоставления типов скобок
также set для удобства проверки типа скобки открывающая/закры-
вающая.

task: 4.7
name: minimum element in stack
time: O(1)
memory: O(n)
рефлексия: добавил в класс метод get_min, расширил push и pop
чтобы обновлять стек для хранения минимальных значений.

task: 4.8
name: average of all elements in stack
time: O(1)
memory: O(n)
рефлексия: добавил в класс метод get_mean, расширил push и pop
чтобы обновляли поле _sum.

task: 4.9
name: postfix expression evaluation
time: O(n)
memory: O(n)
рефлексия: копипастил как в примере a = pop() b = pop() a + b,
нужно переписать на словарь с лямбда функциями.
"""

