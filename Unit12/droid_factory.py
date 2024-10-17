from droids import Droid
import array_queue

def unload_shipment(filename, belt):
    with open(filename) as file:
        for part in file:
            part = part.strip()
            belt.enqueue(part)

def main():
    belt = array_queue.Queue()
    unload_shipment("parts_001_001.txt", belt)
    print(belt)

if __name__ == "__main__":
    main()


