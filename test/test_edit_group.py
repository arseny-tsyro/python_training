# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.group import Group
import random


def test_edit_first_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="sdfsf"))
    old_groups = db.get_group_list()
    target_group = random.choice(old_groups)
    group = Group(name="test")
    group.id = target_group.id
    app.group.edit_by_id(target_group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups = [group if gr.id == group.id else gr for gr in old_groups]
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
