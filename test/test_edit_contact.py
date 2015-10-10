# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.edit_first()

