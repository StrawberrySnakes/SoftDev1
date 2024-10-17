from array_queue import *

def test_create():
    queue = Queue()
    
    assert queue.is_empty()
    assert 0 == len(queue)

def test_enqueue_1():
    queue = Queue()

    queue.enqueue("a")

    assert not queue.is_empty()
    assert 1 == len(queue)
    assert "a" == queue.front()
    assert "a" == queue.back()


def test_enqueue_3():
    queue = Queue()

    queue.enqueue(5)
    queue.enqueue(7)
    queue.enqueue(9)

    assert not queue.is_empty()
    assert 3 == len(queue)
    assert 5 == queue.front()
    assert 9 == queue.back()
    assert "[5, 7, 9]" == str(queue)

def test_dequeue_1():
    queue = Queue()

    queue.enqueue(7)

    value = queue.dequeue()
    

    assert queue.is_empty()
    assert 0 == len(queue)
    assert value == 4
    assert "[]" == str(queue)

def test_dequeue_1():
    queue = Queue()

    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")

    value = queue.dequeue()
    

    assert not queue.is_empty()
    assert 2 == len(queue)
    assert value == "a"
    assert "[b, c]" == str(queue)

def test_enqueue_4():
    queue = Queue()

    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    queue.enqueue(1)

    assert 4 == len(queue)
    


