# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.contact import Contact


def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test", lastname="Last")
    contact.id = old_contacts[0].id
    if app.contact.count() == 0:
        app.contact.create()
    app.contact.edit_first(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

