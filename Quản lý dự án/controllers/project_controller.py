from models.project_model import ProjectModel

class ProjectController:
    @staticmethod
    def get_project(status=None, start_date=None, end_date=None):
        return ProjectModel.get_projects(status=status, start_date=start_date, end_date=end_date)
    
    @staticmethod
    def add_project(project_name, start_date, end_date, status, manager):
        ProjectModel.add_project(project_name, start_date, end_date, status, manager)

    @staticmethod
    def update_project(project_id, project_name, start_date, end_date, status, manager):
        ProjectModel.update_project(project_id, project_name, start_date, end_date, status, manager)

    @staticmethod
    def delete_project(project_id):
        ProjectModel.delete_project(project_id)