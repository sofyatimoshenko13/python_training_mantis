import random
from models.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    app.project.open_projects_page()
    if len(app.soap.get_project_list("administrator", "root")) == 0:
        app.project.create_project(Project(name="project to delete"))
    old_projects = app.soap.get_project_list("administrator", "root")
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list("administrator", "root")
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

