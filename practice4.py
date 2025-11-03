
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price:.2f} USD")
        print("-" * 30)
    def apply_discount(self, percent):
        discount_amount = (percent / 100) * self.price
        self.price -= discount_amoun
book1 = Book("physics", " Newton", 145000000)
book2 = Book("math", "zahrasoofi", 9000000)
print("قبل از تخفیف:")
book1.display_details()
book2.apply_discount(10)
print("پس از اپدیت:")
book1.display_details()
book2.display_details()
