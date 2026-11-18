import random

def test_add_project(app):
    wd = app.wd
    app.session.login("administrator", "root")
    wd.find_element_by_xpath("//a[span[normalize-space()='Управление']]").click()
    wd.find_element_by_css_selector("a[href*='manage_proj_page.php']").click()
    app.project.create_project("new project" + str(random.randint(1, 10000)))
