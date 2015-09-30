# -*- coding: utf-8 -*-
__author__ = 'Arseniy'


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first()
    app.session.logout()
