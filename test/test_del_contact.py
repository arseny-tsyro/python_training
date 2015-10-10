# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.contact import Contact


def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Test"))
    app.contact.delete_first()