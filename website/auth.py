from flask import Blueprint,render_template,request,flash,redirect,url_for,session
import re
from .models import User,Workspace
from . import db
import uuid
from werkzeug.security import generate_password_hash,check_password_hash
import os
from flask import current_app
from .tcopy import copy_template

auth=Blueprint('auth',__name__)


@auth.route('/login',methods=['GET','POST'])

def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('pass1')

        user=User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password,password):
                flash('login success!!',category='success')
                return redirect(f'/workspace/{user.workspace.workid}')
            else:
                flash('incorrect password!!',category='error')
        else:
            flash('email not found!!',category='error')
    return render_template("login.html")

@auth.route('/signup',methods=['GET','POST'])

def signup():
    condition="^\w+[\._]?\w+[@]\w+[.]\w{2,3}$"
    if request.method=='POST':
        email=request.form.get('email')
        name=request.form.get('name')
        pass1=request.form.get('pass1')
        pass2=request.form.get('pass2')
        

        user=User.query.filter_by(email=email).first()
        if user:
            flash("email already exists!!",category="error")
        elif not(re.search(condition,email)):
            flash("Invalid email!!",category="error")
        elif not(re.search("^[a-zA-Z]",name)):
            flash("Invalid name!!",category="error")
        elif len(pass1)<=7:
            flash("Password atleast 8 char!",category="error")
        elif pass1!=pass2:
            flash("Password must be same!!",category="error")
        else:
            session['email']=email
            session['name']=name
            session['pass1']=pass1
            return redirect(url_for('auth.choose_template'))
            

    return render_template("signup.html")

@auth.route('/choose_template',methods=['GET','POST'])

def choose_template():
    if request.method=='POST':
        email=session.get('email')
        name=session.get('name')
        pass1=session.get('pass1')
        workspace= Workspace(workid=str(uuid.uuid4()),name=f'{name}')
        db.session.add(workspace)
        db.session.commit()
        newuser= User(id=str(uuid.uuid4()),email=email,password=generate_password_hash(pass1,method='sha256'),name=name,workid=workspace.workid,workspace=workspace)
        db.session.add(newuser)
        db.session.commit()
        tem=request.form.get('template')
        print("hello",tem)
        user_workspace_folder = os.path.join(current_app.config['WORKSPACE_FOLDER'], workspace.workid)
        user_asset_folder = os.path.join(current_app.config['ASSET_FOLDER'], workspace.workid)
        # Create the user's workspace folder if it doesn't exist
        if not os.path.exists(user_workspace_folder):
            os.makedirs(user_workspace_folder)
            os.makedirs(user_asset_folder)

        # Copy the selected template to the user's workspace folder
        template_folder = os.path.join(current_app.config['TEMPLATES_FOLDER'], tem)
        assets_folder = os.path.join(current_app.config['TEMPLATES_FOLDER'], tem)
        asset_folder = os.path.join(assets_folder, "assets")
        copy_template(template_folder, user_workspace_folder)
        copy_template(asset_folder, user_asset_folder)

        flash("Account created! plz login",category="success")
        return redirect(f'/workspace/{workspace.workid}')
    return render_template("templates.html")