class Compress:
    def __init__(self) -> None:
        self.val = {}
        self.comp = []
    
    def compress(self, txt):
        c = 1
        list = txt.split(' ')
        for i in range(len(list)):
            if not list[i] in self.val:
                self.val[list[i]] = c
                c += 1
        for i in range(len(list)):
            if list[i] in self.val:
                self.comp.append(self.val[list[i]])
        return self.comp, self.val
                
if __name__ == '__main__':
    with open('tdd.txt') as file:
        text_1 = file.read()
        print(text_1)
        a = Compress()
        a.compress(text_1)
        print(a.val)
        print(a.comp)