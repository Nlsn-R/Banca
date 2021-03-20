import os
import csv




MENU = """
                                                                            - M E N Ú -

                                                                        [A]ñadir contacto
                                                                        [ED]itar contacto
                                                                        [B]uscar contacto
                                                                        [E]liminar contacto
                                                                        [L]istar contactos
                                                                        [S]alir
        """

class Contact :

    def __init__( self, name, phone, mail ) :
        self.name = name
        self.phone = phone
        self.mail = mail

class ContactBook :

    def __init__(self) :
        self.contacts = []
    
    def create( self, name, phone, mail ) :
        self.contacts.append(Contact( name, phone, mail ))
        self.save()

    def show_all(self) :
        for contact in self.contacts :

            self.show(contact)

    def show( self, contact ) :
        print("\n")
        print(" "*60,'--- * --- * --- * --- * --- * --- * --- * ---')
        print(" "*60,'Nombre:',contact.name.rjust(37," "))
        print(" "*60,'Teléfono:',contact.phone.rjust(35," "))
        print(" "*60,'Email:',contact.mail.rjust(38," "))
        print(" "*60,'--- * --- * --- * --- * --- * --- * --- * ---')        
    
    def delete( self, name ) :

        for idx, contact in enumerate(self.contacts) :

            if contact.name.lower() == name.lower() :
                del self.contacts[idx]
                self.save()
                break
        else :
            os.system("cls")
            print("\n"*20," "*70,end="")
            print("Contacto no encontrado") 
            input(" "*81)
    
    def search( self, name ) :

        for contact in self.contacts :

            if contact.name.lower() == name.lower() :
                os.system("cls")
                print("\n"*17)
                self.show(contact)
                break
        else :
            os.system("cls")
            print("\n"*20," "*70,end="")
            print("Contacto no encontrado") 
    
    def edit( self, name ) :

        for contact in self.contacts :

            if contact.name.lower() == name.lower() :
                print(" "*62,end="")
                phone = input("Teléfono:           ")
                print(" "*62,end="")
                mail = input("Correo electronico: ")
                self.save()
                break
        else :
            os.system("cls")
            print("\n"*20," "*70,end="")
            print("Contacto no encontrado") 
            input(" "*81)


    def save(self) :
        with open( "contact.csv", "w") as f :
            writer = csv.writer(f)
            writer.writerow( ('NAME', 'PHONE', 'MAIL') )

            for contact in self.contacts:
                writer.writerow( (contact.name, contact.phone, contact.mail) )




def run() :
    contact_book = ContactBook()


    try:
        with open('contact.csv', 'r') as f :
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                elif idx % 2 != 0:
                    continue
                else:
                    contact_book.create(row[0], row[1], row[2])
    except :
        pass


    while True:
        os.system("cls")
        print("\n"*15)
        print(MENU,"\n")
        command = input(" "*81).lower()

        if command == 'a':
            os.system("cls")
            print("\n"*20," "*61,end="")
            name = input("Nombre:             ")
            print(" "*62,end="")
            phone = input("Teléfono:           ")
            print(" "*62,end="")
            mail = input("Correo electronico: ")
            contact_book.create( name, phone, mail )

        elif command == 'ed':
            os.system("cls")
            print("\n"*20," "*61,end="")
            name = input("Nombre:             ")
            contact_book.edit(name)

        elif command == 'b':
            os.system("cls")
            print("\n"*20," "*70,end="")
            name = input("Nombre: ")
            contact_book.search(name)
            input(" "*81)

        elif command == 'e':
            os.system("cls")
            print("\n"*20," "*70,end="")
            name = input("Nombre: ")
            contact_book.delete(name)

        elif command == 'l':
            os.system("cls")
            contact_book.show_all()
            input(" "*81)

        elif command == 's':
            os.system("cls")
            break

        else:
            os.system("cls")
            print("\n"*20," "*73,end="")
            print("Comando invalido")
            input(" "*81)






if __name__ == "__main__" :
    run()