from flask import Blueprint,render_template
from .models import Workspace
import os
from flask import current_app

workspaces=Blueprint('workspaces',__name__)

@workspaces.route('/workspace/<workspace_id>', methods=['GET','POST'])
def work(workspace_id):
    workspace= Workspace.query.get(workspace_id)
    user_workspace_folder = os.path.join("/users/", workspace_id)
    return render_template(f'/users/{workspace_id}/home.html',workspace=workspace)

@workspaces.route('/workspace/<workspace_id>/skills', methods=['GET','POST'])
def skills(workspace_id):
    workspace= Workspace.query.get(workspace_id)
    return render_template(f'/users/{workspace_id}/skill.html',workspace=workspace)


