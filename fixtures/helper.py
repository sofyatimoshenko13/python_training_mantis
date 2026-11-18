class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, name):
        wd = self.app.wd
        wd.find_element_by_xpath("//button[normalize-space()='Создать новый проект']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").send_keys(name)
        wd.find_element_by_css_selector("input[value='Добавить проект']").click()
