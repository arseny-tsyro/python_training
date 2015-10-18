# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.contact import Contact
import pytest
import string
import random


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
            home_num="", mobile_num="", work_num="", fax_num="", email2="", email3="", homepage="", byear="", ayear="",
            address2="", phone2="", notes="")] + [
    Contact(firstname=random_string("name", 10), middlename="M.", lastname=random_string("lastn", 10),
            nickname="Nickie", title="sdfsdf", company="fdsfsdf", address=random_string("address", 10),
            home_num=random_string("home", 10), mobile_num=random_string("mobile", 10), work_num="+7 21212",
            fax_num="50", email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homepage="asdfsad.com", byear="1999", ayear="1980",
            address2="fdsafasdf", phone2=random_string("pnone2", 10), notes="asdfd")
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
