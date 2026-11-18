import random
from models.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    old_projects = app.project.get_project_list()
    project = Project(name="new_project_" + str(random.randint(1, 10000)))
    app.project.create_project(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

