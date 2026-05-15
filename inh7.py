class Publication:
    def __init__(self):
        self.title = ""
        self.price = 0.0

    def get_data(self):
        self.title = input("Enter the Title : ")
        self.price = float(input("Enter the Price : "))

    def put_data(self):
        print("Title    :", self.title)
        print("Price    :", self.price)

class Book(Publication):
    def __init__(self):
        super().__init__()
        self.pagecount = 0

    def get_data(self):
        super().get_data()
        self.pagecount = int(input("Enter number of pages  :  "))

    def put_data(self):
        super().put_data()
        print("Pages    :", self.pagecount)

class DVD(Publication):
    def __init__(self):
        super().__init__()
        self.playing_time = 0.0

    def get_data(self):
        super().get_data()
        self.playing_time = float(input("Enter playing time : "))

    def put_data(self):
        super().put_data()
        print("Playing time:", self.playing_time)

class Inh7:
    @staticmethod
    def main():
        book = Book()
        dvd = DVD()

        print("Enter the Book details")
        book.get_data()

        print("Enter the DVD details")
        dvd.get_data()

        print("\n\nBook Details")
        print("-------------")
        book.put_data()

        print("\n\nDVD Details")
        print("---------------")
        book.put_data()
Inh7.main()
        
