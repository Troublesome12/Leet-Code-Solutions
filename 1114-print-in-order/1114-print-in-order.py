class Foo:
    def __init__(self):
        self.first_is_done = False
        self.second_is_done = False


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_is_done = True


    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.first_is_done:
            pass
    
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_is_done = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.second_is_done:
            pass
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()