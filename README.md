# Reflection

## Test Failure
...
(cidm3312) PS C:\Users\ally\CIDM3312\book-catalog> uv run python manage.py test
Found 1 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_book_appears_on_books_page (catalog.tests.BookPageTest.test_book_appears_on_books_page)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\Users\ally\CIDM3312\book-catalog\catalog\tests.py", line 19, in test_book_appears_on_books_page
    self.assertContains(response, "Unique Test Book 8472")
    ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: False is not true : Couldn't find 'Unique Test Book 8472' in the following response
b'<html>\n<head>\n    <title>Book Catalog</title>\n</head>\n<body>\n    <h1> Book Catalog </h1>\n    <hr>\n    \n    <nav>\n        <a href="/">Books</a>\n        <a href="/publishers/">Publishers</a>\n        <a href="/reviews/">Reviews</a>\n    </nav>\n    <hr>\n\n    \n\n<h1>Books</h1>\n\n\n\n\n\n</body>\n</html>'

----------------------------------------------------------------------
Ran 1 test in 0.011s

FAILDED (failures=1)
...

the failure above shows that the book created in the test run does not display on the books page, this is due to the
inserted command "queryset = Book.objects.none()" which I placed inside the BookView to break the test without breaking
the actual page.