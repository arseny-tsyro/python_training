# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.contact import Contact
from model.group import Group
import random


def test_add_some_contact_to_some_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="new group"))
    if len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Mike", lastname="Smith"))
    groups_from_db = orm.get_group_list()
    group = random.choice(groups_from_db)
    contact = random.choice(orm.get_contact_list())
    app.contact.add_to_group(contact, group)

    contact_in_group = False
    for gr in groups_from_db:
        if gr.name == group.name and contact in orm.get_contacts_in_group(gr):
            contact_in_group = True
    assert contact_in_group
