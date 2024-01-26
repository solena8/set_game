from dataclasses import dataclass

bidul_machin: int
bidul_machin = 12
print(bidul_machin)
bidul_machin = 666
print(bidul_machin)

my_var_str: str = "Hello, it's me from the"
print(my_var_str)
my_var_str = "zzzz"
print(my_var_str)

my_var_bool: bool = True

my_var_list: list[str] = ["zzz", "fff", "jjj"]

book: str = "Dans un univers lointain, très lointain, "
book_v2: list[str] = ["Page 1 content", "Page 2 content"]


@dataclass
class Chapter:
    chapter_title: str
    pages: list[str]

    # Methods
    def number_of_pages(self) -> int:
        return len(self.pages)

@dataclass
class Book:
    # Attributes
    chapters: Chapter
    title: str
    author: str

doubidou_chapter: Chapter = Chapter(chapter_title="Doubidou", pages=["Page 1 content", "Page 2 content", "Page 3 content", "Page 4 content"])

# harry_1: Book = Book(pages=["Page 1 content", "Page 2 content"],
#                            title="Happry potter et la chambre des secrets",
#                            author="JK Rowling")

lord_of_the_ring: Book = Book(chapters=doubidou_chapter,
                           title="Le seigneur des anneaux - La commu de l'anal",
                           author="Tolkien")

print(lord_of_the_ring)

# print("pages", harry_1.title, harry_1.number_of_pages())
# print("pages", lord_of_the_ring.title, lord_of_the_ring.number_of_pages())