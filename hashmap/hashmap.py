class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    def __init__(self):
        self.store = [None for _ in range(16)]

    def get(self, key):
        index = hash(key) & 15
        if self.store[index] is None:
            return None
        n = self.store[index]
        while True:
            if n.key == key:
                return n.value
            else:
                if n.next:
                    n = n.next
                else:
                    return None

    def put(self, key, value):
        nd = Node(key, value)
        index = hash(key) & 15
        n = self.store[index]
        if n is None:
            self.store[index] = nd
        else:
            if n.key == key:
                n.value = value
            else:
                while n.next:
                    if n.key == key:
                        n.value = value
                        return
                    else:
                        n = n.next
                n.next = nd


if __name__ == '__main__':
    hashmap = HashMap()

    hashmap.put('1', 'something at 1')
    hashmap.put('2', 'something at 2')
    hashmap.put('3', 'something at 3')
    hashmap.put('4', 'something at 4')
    hashmap.put('5', 'something at 5')
    hashmap.put('6', 'something at 6')
    hashmap.put('7', 'something at 7')
    hashmap.put('8', 'something at 8')
    hashmap.put('9', 'something at 9')
    hashmap.put('10', 'something at 10')

    print(hashmap.get('1'))
    print(hashmap.get('2'))
    print(hashmap.get('3'))
    print(hashmap.get('4'))
    print(hashmap.get('5'))
    print(hashmap.get('6'))
    print(hashmap.get('7'))
    print(hashmap.get('8'))
    print(hashmap.get('9'))
    print(hashmap.get('10'))
