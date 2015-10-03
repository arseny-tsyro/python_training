# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="adfsdf", header="asdfasdf", footer="asfasdfds"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


def test_del_first_group(app):
    app.group.delete_first()


def test_edit_first_group(app):
    app.group.edit_first(name="Edited name")
