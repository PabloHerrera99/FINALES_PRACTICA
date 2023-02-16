class TemaMusical:
    
    def __init__(self, code, name, time, author):
        self.code = code
        self.name = name
        self.time = time
        self. author = author

if __name__ == '__main__':
    
    m = TemaMusical('', 'Despacito', 281, 'Luis Fonzi')
    print(m.__dict__)
    