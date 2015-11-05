# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.contact import Contact
import random


def test_edit_first_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create()
    old_contacts = db.get_contact_list()
    target_contact = random.choice(old_contacts)
    contact = Contact(firstname="Test", lastname="Last")
    contact.id = target_contact.id
    app.contact.edit_by_id(target_contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts = [contact if con.id == contact.id else con for con in old_contacts]
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
