# -*- coding: utf-8 -*-
__author__ = 'Arseniy'
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def load_groups_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/group.pgp") and len(wd.find_element_by_name("new")) > 0:
            return
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.load_groups_page()
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
        self.group_cache = None

    def edit_first(self, group):
        self.edit_by_index(group, 0)

    def edit_by_index(self, index, group):
        wd = self.app.wd
        self.load_groups_page()
        self.select_by_index(index)
        # go to edit page
        wd.find_element_by_name("edit").click()
        # edit info
        if group.name:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(group.name)
        if group.header:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(group.header)
        if group.footer:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit changes
        wd.find_element_by_name("update").click()
        self.group_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        wd = self.app.wd
        self.load_groups_page()
        self.select_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.load_groups_page()
        self.group_cache = None

    def delete_by_id(self, id):
        wd = self.app.wd
        self.load_groups_page()
        self.select_by_id(id)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.load_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.load_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.load_groups_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


