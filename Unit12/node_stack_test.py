from node_stack import *

def test_create():
    stack = Stack()
    assert stack.is_empty()

def test_push_1():
    stack = Stack()

    stack.push(5)

    assert not stack.is_empty()
    assert 5 == stack.peek()
    assert "[5]" == str(stack)
    assert 1 == len(stack)


def test_push_3():
    stack = Stack()

    stack.push("a")
    stack.push("b")
    stack.push("c")

    assert not stack.is_empty()
    assert "c" == stack.peek()
    assert "[c, b, a]" == str(stack)
    assert 3 == len(stack)

def test_pop_1():
    stack = Stack()

    stack.push("z")

    value = stack.pop()

    assert stack.is_empty()
    assert value == "z"
    assert 0 == len(stack)
    assert "[]" == str(stack)

def test_pop_3():
    stack = Stack()

    stack.push("z")
    stack.push("y")
    stack.push("x")


    value = stack.pop()

    assert not stack.is_empty()
    assert value == "x"
    assert 2 == len(stack)
    assert "[y, z]" == str(stack)
