# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.group import Group
import random


def test_del_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        ui = sorted(app.group.get_group_list(), key=Group.id_or_max)
        gr = sorted(map(lambda x: Group(id=x.id, name=x.name.strip()), new_groups), key=Group.id_or_max)
        assert gr == ui
