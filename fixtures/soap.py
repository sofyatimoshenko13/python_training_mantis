from suds.client import Client
from suds import WebFault
from models.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.28.4/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client("http://localhost/mantisbt-2.28.4/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            return [Project(id=str(p.id), name=p.name) for p in projects]
        except WebFault:
            return []
