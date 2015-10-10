# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(
        Contact(firstname="asdf", middlename="asdfasd", lastname="fdsfsd", nickname="sdfsd", title="sdfsdf",
                company="fdsfsdf", address="sdfdf", home_num="1212", mobile_num="12212", work_num="21212", fax_num="50",
                email2="afasd@adf", email3="asdsd@asdf", homepage="asdfsad.com", byear="1999", ayear="1980",
                address2="fdsafasdf", phone2="dsafdsf", notes="asdfd"))


def test_add_empty_contact(app):
    app.contact.create(
        Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_num="",
                mobile_num="", work_num="", fax_num="", email2="", email3="", homepage="", byear="", ayear="",
                address2="", phone2="", notes=""))