__author__ = 'Arseniy'
from pytest_bdd import given, when, then
from model.group import Group
import random
import pytest


@pytest.allure.step('Given a group list')
@given('a group list')
def group_list(db):
    return db.get_group_list()


@pytest.allure.step('Given a group with name={name}, header={header} and footer={footer}')
@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)


@pytest.allure.step('Given a non-empty group list')
@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="gr name"))
    return db.get_group_list()


@pytest.allure.step('Given a random group from the list')
@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    with pytest.allure.step('When I delete the group {} from the list'.format(random_group)):
        app.group.delete_by_id(random_group.id)


@when('I add the group to the list')
def add_new_group(app, new_group):
    with pytest.allure.step('When I add the group {} to the list'.format(new_group)):
        app.group.create(new_group)


@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    with pytest.allure.step('Then the new group list is equal to the old list with the added group'):
        old_groups = group_list
        new_groups = db.get_group_list()
        old_groups.append(new_group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


@then('the new group list is equal to the old list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    with pytest.allure.step('Then the new group list is equal to the old list without the deleted group'):
        old_groups = non_empty_group_list
        new_groups = db.get_group_list()
        old_groups.remove(random_group)
        assert old_groups == new_groups
    if check_ui:
        with pytest.allure.step('Also check UI'):
            ui = sorted(app.group.get_group_list(), key=Group.id_or_max)
            gr = sorted(map(lambda x: Group(id=x.id, name=x.name.strip()), new_groups), key=Group.id_or_max)
            assert gr == ui

