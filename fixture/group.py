# -*- coding: utf-8 -*-
__author__ = 'Arseniy'


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def load_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        # go to groups page
        wd.find_element_by_link_text("groups").click()
        # create new group
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit
        wd.find_element_by_name("submit").click()
        self.load_groups_page()

    def delete_first(self):
        wd = self.app.wd
        # go to groups page
        wd.find_element_by_link_text("groups").click()
        # check the first group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.load_groups_page()
