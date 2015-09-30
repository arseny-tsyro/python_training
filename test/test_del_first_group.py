# -*- coding: utf-8 -*-
__author__ = 'Arseniy'


def test_del_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_first()
    app.session.logout()