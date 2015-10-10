# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="adfsdf", header="asdfasdf", footer="asfasdfds"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
