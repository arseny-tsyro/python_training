# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
import random
import string
import os
import jsonpickle
import getopt
import sys
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [] + [
    Contact(firstname=random_string("name", 10), middlename=random_string("mid", 3),
            lastname=random_string("lastn", 10), nickname="Nickie", title="sdfsdf", company="fdsfsdf",
            address=random_string("address", 10), home_num=random_string("home", 10),
            mobile_num=random_string("mobile", 10), work_num="+7 21212",
            fax_num="50", email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homepage="asdfsad.com", byear="1999", ayear="1980",
            address2="fdsafasdf", phone2=random_string("pnone2", 10), notes="asdfd")
    for i in range(5)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))