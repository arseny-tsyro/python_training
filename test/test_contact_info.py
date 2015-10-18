__author__ = 'Arseniy'
from model.contact import Contact
from random import randrange
import re


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