__author__ = 'Arseniy'
from sys import maxsize


class Contact:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home_num=None, mobile_num=None, work_num=None, fax_num=None, email2=None, email3=None,
                 homepage=None, byear=None, ayear=None, address2=None, phone2=None, notes=None,
                 all_phones_from_home_page=None):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home_num = home_num
        self.mobile_num = mobile_num
        self.work_num = work_num
        self.fax_num = fax_num
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.all_phones_from_home_page = all_phones_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and \
               self.lastname == other.lastname

    def __repr__(self):
        return "(%s: %s %s)" % (self.id, self.firstname, self.lastname)