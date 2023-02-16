class Mail:
    def __init__(self, mail, tipo, persona_id = None) -> None:
        self._Mail__mail = mail
        self._Mail__tipo = tipo
        self._Mail__mail_id = None
        self._Mail__persona_id = persona_id
        
    
    def __str__(self) -> str:
        
        if self._Mail__mail.find('@') >= 1:
            return self._Mail__tipo + '/' + self._Mail__mail + ' - ' + str(self._Mail__persona_id)
        else:
            return str('None')     

if __name__ == '__main__':
    p = Mail('valid@email.com', 'personal', 1)
    print(p.__dict__)
    print(p._Mail__persona_id)
    print(p)
    #p = Mail('b@b.com', 'personal')
    #print(p.__dict__)
    #print(str(p))
        