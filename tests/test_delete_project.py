import random
from models.project import Project


def test_delete_project(app, config):
    username = config['webadmin']['username']
    password = config['webadmin']['password']
    app.session.login(username, password)
    app.project.open_projects_page()
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.create_project(Project(name="project to delete"))
    old_projects = app.soap.get_project_list(username, password)
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = app.soap.get_project_list(username, password)
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

