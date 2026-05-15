# 📚 Publication, Book & DVD Management System in Python

## 📌 Description

This Python program demonstrates **Hierarchical Inheritance** using a parent class `Publication` and two child classes:

* `Book`
* `DVD`

It stores and displays details related to books and DVDs.

---

## 🚀 Features

* Demonstrates **inheritance** and **method overriding**
* Uses `super()` method
* Accepts user input
* Displays:

  * Book details
  * DVD details

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `Publication`

Contains common attributes:

* `title`
* `price`

Methods:

* `get_data()`
* `put_data()`

---

### 2️⃣ Child Class – `Book`

Inherits from `Publication`.

Adds:

* `pagecount`

Overrides:

* `get_data()`
* `put_data()`

---

### 3️⃣ Child Class – `DVD`

Inherits from `Publication`.

Adds:

* `playing_time`

Overrides:

* `get_data()`
* `put_data()`

---

## 🧬 Inheritance Structure

```text id="1y0gpm"
           Publication
            /      \
           /        \
        Book        DVD
```

---

## 💻 Code

```python id="v8m3qx"
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
        self.pagecount = int(input("Enter number of pages : "))

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
        print("Playing time :", self.playing_time)


class Inh7:
    @staticmethod
    def main():
        book = Book()
        dvd = DVD()

        print("Enter the Book details")
        book.get_data()

        print("\nEnter the DVD details")
        dvd.get_data()

        print("\n\nBook Details")
        print("-------------")
        book.put_data()

        print("\n\nDVD Details")
        print("-------------")
        dvd.put_data()


Inh7.main()
```

---

## ⚠️ Bug in Your Original Code

In your code:

```python id="t6k2pl"
book.put_data()
```

was used for DVD details.

👉 It should be:

```python id="m4x9qa"
dvd.put_data()
```

Otherwise, book details print twice.

---

## ▶️ Example Output

```id="s7m3zx"
Enter the Book details
Enter the Title : Python Basics
Enter the Price : 450
Enter number of pages : 320

Enter the DVD details
Enter the Title : Python Tutorial DVD
Enter the Price : 299
Enter playing time : 2.5


Book Details
-------------
Title    : Python Basics
Price    : 450.0
Pages    : 320


DVD Details
-------------
Title    : Python Tutorial DVD
Price    : 299.0
Playing time : 2.5
```

---

## 🧠 Key Concepts

### ✔ Hierarchical Inheritance

Both:

* `Book`
* `DVD`

inherit from:

* `Publication`

---

### ✔ Method Overriding

Child classes redefine:

* `get_data()`
* `put_data()`

---

### ✔ `super()` Keyword

Used to call parent class methods:

```python id="n8q1pt"
super().get_data()
```

---

## 📚 Concepts Used

* Class & Object
* Hierarchical Inheritance
* Method Overriding
* User input
* `super()` method

---

## 🎯 Advantages

* Reuse common publication data
* Cleaner and modular code
* Easy to extend with new media types

---

## 🔧 Future Improvements

* Add Magazine class
* Store multiple books/DVDs in lists
* Add issue date & author fields
* Create menu-driven system

---

## 📄 License

This project is open-source and free to use.
