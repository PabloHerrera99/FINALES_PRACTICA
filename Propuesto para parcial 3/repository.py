#from mail import Mail
from persona import Persona
from mail import Mail

class Repository:
    def __init__(self):
        self.personas = {}
        self.mails = []
        self.persona_id = 0
        self.mail_id = 0
    
    def add_persona(self,persona):
        self.persona_id +=1
        self.personas[self.persona_id] = str(persona)
        
        return self.persona_id 
        
    def add_mail(self, mail):
        self.mail_id +=1
        self.mails.append(str(self.mail_id) + ' - ' + str(mail))
        
        
    def to_string(self, persona_id = None, mail_id = None):
        mail = ''
        if persona_id != None:
            for i in range(len(self.mails)):
                if str(self.mails[i])[-1] == str(persona_id):
                    mail = mail + '\n'+ '    ' + self.mails[i]
            return str(persona_id) + '/' + self.personas[persona_id] + str(mail)
        if mail_id != None:
            for i in range(len(self.mails)):
                if str(self.mails[i])[0] == str(mail_id):
                    mail = self.mails[i]
                    persona_id = str(self.mails[i])[-1]
            return str(mail) + '\n' + '    ' + str(persona_id) + '/' + self.personas[int(persona_id)]
    


if __name__ == '__main__':
    r = Repository()
    p1 = r.add_persona(Persona(apellido='Doe', nombre='John'))
    p2 = r.add_persona(Persona(apellido='Doe', nombre='Jane'))
    r.add_mail(Mail('a@a.com', 'personal', p1))
    r.add_mail(Mail('a@j.com', 'personal', p2))
    r.add_mail(Mail('b@a.com', 'laboral', p1))
    r.add_mail(Mail('b@j.com', 'laboral', p2))
    print(r.to_string(persona_id=1))
    print(r.to_string(persona_id=2))
    print(r.to_string(mail_id=3))