
class Author:
    all = []
    def __init__(self, name) -> None:
        if isinstance(name, str):
            self.name = name
        else:
            raise Exception("Name must be a string")
    
        Author.all.append(self)

        pass
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [book.book for book in Contract.all if book.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])

    pass


class Book:
    all = []
    def __init__(self, title) -> None:
        if isinstance(title, str):
            self.title = title
        else:
            raise Exception("Title must be a string")
    
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [author.author for author in Contract.all if author.book == self]
    pass


class Contract:
    all = []
    def __init__(self, author, book, date, royalties) -> None:
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Author must be an instance of Author class")
        
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Book must be an instance of Book class")

        if isinstance(date, str):
            self.date = date
        else:
            raise Exception("Date must be a string")
        
        if isinstance(royalties, int):
            self.royalties = royalties
        else:
            raise Exception("Royalties must be an integer")

        Contract.all.append(self)
        
        pass

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
