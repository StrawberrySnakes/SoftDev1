"""Dessa Sahpiro"""
from list_stack import Stack


def test_init():
    #setup
    stack = Stack()

    #analyze
    assert stack.is_empty()
    assert len(stack) == 0

def test_repr():
    #setup
    stack = Stack()
    #analyze
    assert repr(stack) == "[]"
    stack.push(1)
    assert repr(stack) == "[1]"
    stack.push(2)
    assert repr(stack) == "[1, 2]"

def test_is_empty():
    #setup
    stack = Stack()
    #analyze
    assert stack.is_empty()
    #setup
    stack.push(1)
    #analyze
    assert not stack.is_empty()
    #setup
    stack.pop()
    #analyze
    assert stack.is_empty()

def test_len():
    #setup
    stack = Stack()
    #analyze
    assert len(stack) == 0
    #setup
    stack.push(1)
    #analyze
    assert len(stack) == 1
    #setup
    stack.push(2)
    #analyze
    assert len(stack) == 2

def test_peek():
    #setup
    stack = Stack()
    stack.push(1)
    #analyze
    assert stack.peek() == 1
    #setup
    stack.push(2)
    #analyze
    assert stack.peek() == 2

def test_pop():
    #setup
    stack = Stack()
    stack.push(1)
    stack.push(2)
    #analyze
    assert stack.pop() == 1
    assert len(stack) == 1
    assert stack.pop() == 2
    assert len(stack) == 0

def test_push():
    #setup
    stack = Stack()
    stack.push(1)
    #analyze
    assert stack.peek() == 1
    assert len(stack) == 1
    #setup
    stack.push(2)
    #analyze
    assert stack.peek() == 2
    assert len(stack) == 2