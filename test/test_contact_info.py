__author__ = 'Arseniy'
from model.contact import Contact
from random import randrange
import re


def test_phones_on_home_page(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    for con_db in contacts_from_db:
        con_ui = list(filter(lambda x: x.id == con_db.id, contacts_from_home_page))[0]
        assert con_ui.all_phones_from_home_page == merge_phones_like_on_home_page(con_db)


def test_phones_on_contact_view_page(app, db):
    contacts_from_db = db.get_contact_list()
    for con_db in contacts_from_db:
        text_from_view_page = app.contact.get_text_from_view_page_by_id(con_db.id)
        phones_from_db = get_phones_like_on_view_page(con_db)
        for phone in phones_from_db:
            assert phone in text_from_view_page


def test_info_from_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="John", lastname="Snow", address="Hollywood, 11", email2="john@ya.ru",
                                   email3="snow@hot.com", work_num="+7 999 666 777"))
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(con):
    emails = [con.email, con.email2, con.email3]
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, emails)))


def merge_phones_like_on_home_page(con):
    phones = [con.home_num, con.mobile_num, con.work_num, con.phone2]
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, phones))))


def get_phones_like_on_view_page(con):
    phones = []
    if not is_empty(con.home_num):
        phones.append("H: %s" % con.home_num)
    if not is_empty(con.mobile_num):
        phones.append("M: %s" % con.mobile_num)
    if not is_empty(con.work_num):
        phones.append("W: %s" % con.work_num)
    if not is_empty(con.phone2):
        phones.append("P: %s" % con.phone2)
    return phones


def is_empty(tel):
    return (tel is None) or (tel == '')
