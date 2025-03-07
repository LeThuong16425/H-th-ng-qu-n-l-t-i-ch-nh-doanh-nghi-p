from flask import Flask, render_template, request, redirect, url_for
from controllers.project_controller import ProjectController
from controllers.news_controller import NewsController

app = Flask(__name__)

@app.route('/')
def index():
    news = NewsController.get_all_news()
    return render_template('news.html', news=news)

@app.route('/projects')
def projects():
    status = request.args.get('status')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    projects = ProjectController.get_projects(status=status, start_date=start_date, end_date=end_date)
    return render_template('projects_list.html', projects=projects)

@app.route('/add', methods=['GET', 'POST'])
def add_project():
    if request.method == 'POST':
        project_name = request.form['project_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        status = request.form['status']
        manager = request.form['manager']
        ProjectController.add_project(project_name, start_date, end_date, status, manager)
        return redirect(url_for('projects'))
    return render_template('add_edit_project.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_project(id):
    if request.method == 'POST':
        project_name = request.form['project_name']
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        status = request.form['status']
        manager = request.form['manager']
        ProjectController.update_project(id, project_name, start_date, end_date, status, manager)
        return redirect(url_for('projects'))
    return render_template('add_edit_project.html', project=ProjectController.get_project(id))

@app.route('/delete/<int:id>')
def delete_project(id):
    ProjectController.delete_project(id)
    return redirect(url_for('projects'))

@app.route('/project/<int:id>')
def project_details(id):
    project = ProjectController.get_project(id)
    if not project:
        return "Project not found", 404
    return render_template('project_details.html', project=project)
@app.route('/add_news', methods=['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        NewsController.add_news(title, content)
        return redirect(url_for('index'))  # Redirect back to the news page

    return render_template('add_news.html')


if __name__ == '__main__':
    app.run(debug=True)
