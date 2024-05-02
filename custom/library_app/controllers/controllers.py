# -*- coding: utf-8 -*-
from odoo import http

class Books(http.Controller):

    @http.route("/library/books")
    def list(self, **kwargs):
        Book = http.request.env["library.book"]
        books = Book.search([])
        for book in books:
            print(book)

        return http.request.render(
            "library_app.book_list_template",
            {"books": books}
        )