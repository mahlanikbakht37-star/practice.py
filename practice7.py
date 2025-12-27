import csv

class Contact:
    def __init__(self, name, phone):
        if not phone.isdigit():
            raise ValueError("phone bayad adadi bashe")

        self.name = name
        self.phone = phone


class PhoneBook:
    def __init__(self):
        self.list = []

    def add_contact(self, name, phone):
        c = Contact(name, phone)
        self.list.append(c)

    def show_all(self):
        if len(self.list) == 0:
            print("hich mokhatabi vojood nadare")
            return

        for c in self.list:
            print(c.name, " -> ", c.phone)

    def save_csv(self, file_name):
        with open(file_name, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["name", "phone"])

            for c in self.list:
                writer.writerow([c.name, c.phone])

        print("zakhire shod")

    def load_csv(self, file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.list = []

                for row in reader:
                    try:
                        c = Contact(row["name"], row["phone"])
                        self.list.append(c)
                    except ValueError:
                        pass  # phone ghalat bod

        except FileNotFoundError:
            print("file peyda nashod")


pb = PhoneBook()
pb.load_csv("contacts.csv")

while True:
    print("\n1- ezafe kardan")
    print("2- namayesh")
    print("3- zakhire va exit")

    try:
        cmd = int(input("entekhab: "))
    except ValueError:
        print("adad vared kon")
        continue

    if cmd == 1:
        n = input("name: ")
        p = input("phone: ")

        try:
            pb.add_contact(n, p)
            print("ok add shod")
        except ValueError:
            print("phone eshtebah ast")

    elif cmd == 2:
        pb.show_all()

    elif cmd == 3:
        pb.save_csv("contacts.csv")
        break

    else:
        print("ghezine eshtebah")
