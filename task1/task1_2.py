from task1 import LinkedList, Node


def linked_list_sum(l1, l2):
    if l1.len() != l2.len():
        return None
    result = LinkedList()
    l1_node = l1.head
    l2_node = l2.head
    while l1_node is not None:
        result_node = Node(l1_node.value + l2_node.value)
        result.add_in_tail(result_node)
        l1_node = l1_node.next
        l2_node = l2_node.next
    return result


"""
task: 1.1
name: delete node from linked list method
time: O(n)
memory: O(1)
рефлексия: задачу делает сложной обработка крайних случаев с удалением head, tail или
единственным элементом в списке. При решении были идеи хранить либо текущий элемент и
проверять следущий, но тогда возникала проблема при обработке связанного списка с 1
элементом, который нужно удалить. Думал добавить фиктивный head, но не стал, когда
прочитал материал следующего задания. Другого решения, кроме текущего, с хранением
ссылки на предыдущий элемент я не нашёл.


task: 1.2
name: option to delete all occurse of val in linked list
time: O(n)
memory: O(1)
рефлексия: не влияет на сложность, главное корректно обновлять ссылку на предыдущую
ноду.


task: 1.3
name: clean linked list method
time: O(1)
memory: O(1)
рефлексия: не нужно очищать вручную, благодаря сборщику мусора, можно просто удалить
все ссылки на элементы списка.


task: 1.4
name: method that searches linked list and returns list of nodes
time: O(n)
memory: O(n)
рефлексия: не вижу способов оптимизации.


task: 1.5
name: len method
time: O(n)
memory: O(1)
рефлексия: можно было бы хранить len в классе, но нужно было бы обновлять его каждый
раз при добавлении или удалении элементов, тогда бы временная O была бы константой.


task: 1.6
name: insert new node into linked list
time: O(1)
memory: O(1)
рефлексия: благодаря тестам заметил, что не обрабатываю случай, когда afterNode == None,
при этом список не пуст. В целов выглядит не очень, возможно, можно написать чище.


task: 1.7
name: tests
time: O(n)
memory: O(n)
рефлексия: использовал pytest, параметризацию и фикстуры. В фикстурах особого смысла
не было, можно было написать как функции, т.к. расширения тестов тут не ожидается,
но использовал их для чистоты и потому, что так советуют.


task: 1.8
name: function for creation new linked list where l[n] = l1[n] + l2[n]
time: O(n)
memory: O(n)
рефлексия: O(n) на одновременный обход двух списков и O(n) памяти на новый, также
не вижу алтернативных решений. Теоритически можно использовать рекурсию, но пользы
от этого подхода не нахожу.
"""

