# -*- coding: utf-8 -*-
__author__ = 'Arseniy'


def test_del_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first()
    app.session.logout()