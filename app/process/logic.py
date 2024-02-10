from ..models import Book


class Catalog:

    @staticmethod
    def get_books():
        books = Book.objects.all()
        return books

    # 検索
    @staticmethod
    def search_book(search_title: str):
        searched_books = Book.objects.filter(title__icontain=search_title)
        return searched_books

    @staticmethod
    def display_book_detail(isbn: str):
        try:
            book = Book.objects.get(isbn=isbn)
        except Book.DoesNotExist:
            # Book モデルにおける DoesNotExist 例外の処理
            print("指定されたISBNの書籍は存在しません。")
        return book
