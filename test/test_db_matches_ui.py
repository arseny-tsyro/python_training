__author__ = 'Arseniy'
from model.group import Group
from model.contact import Contact


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = map(lambda x: Group(id=x.id, name=x.name.strip()), db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contact_list()
    db_list = map(lambda x: Contact(id=x.id, firstname=x.firstname.strip(), lastname=x.lastname.strip()),
                  db.get_contact_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
