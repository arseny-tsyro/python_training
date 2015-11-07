__author__ = 'Arseniy'
from fixture.orm import ORMFixture
from model.group import Group
from model.contact import Contact

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    gr = db.find_group_by_id(Group(id=145))
    db.add_contact_to_group(Contact(id=67), gr)
finally:
    pass # db.destroy()