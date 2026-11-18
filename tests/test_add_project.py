import random
from models.project import Project


def test_add_project(app, config):
    username = config['webadmin']['username']
    password = config['webadmin']['password']
    app.session.login(username, password)
    app.project.open_projects_page()
    old_projects = app.soap.get_project_list(username, password)
    project = Project(name="new_project_" + str(random.randint(1, 10000)))
    app.project.create_project(project)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
