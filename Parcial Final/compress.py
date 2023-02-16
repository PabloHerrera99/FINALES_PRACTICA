class Compress:
       
    def __init__(self) -> None:
        self.val = {}
        self.comp = []
    
    def compress(self, txt):
        tex = txt.split(' ')
        i = 1
        for x in tex:
            if not x in self.val:
                self.val.update({x : i})
                i += 1
            else:
                pass
            
        for x in tex:
            self.comp.append(self.val.get(x))
        
        return self.comp, self.val

if __name__ == '__main__':
    with open('tdd.txt') as file:
            text_1 = file.read() 
    compress = Compress()
    compressed, values = compress.compress(text_1)
    print(compressed)
    print(values)