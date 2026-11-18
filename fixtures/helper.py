from models.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//button[normalize-space()='Создать новый проект']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_css_selector("input[value='Добавить проект']").click()

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[span[normalize-space()='Управление']]").click()
        wd.find_element_by_css_selector("a[href*='manage_proj_page.php']").click()

    def get_project_list(self):
        wd = self.app.wd
        self.open_projects_page()
        projects = []
        for element in wd.find_elements_by_css_selector("a[href*='manage_proj_edit_page.php?project_id=']"):
            text = element.text.strip()
            href = element.get_attribute("href")
            project_id = href.split("project_id=")[1]
            projects.append(Project(name=text, id=project_id))
        return projects

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_css_selector("a[href*='manage_proj_edit_page.php?project_id=%s']" % id).click()
        wd.find_element_by_css_selector("button[formaction='manage_proj_delete.php']").click()
        wd.find_element_by_css_selector("input[value='Удалить проект']").click()
