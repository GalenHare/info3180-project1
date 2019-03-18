"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.forms import UploadForm
from werkzeug.utils import secure_filename
from app.models import UserProfile
from werkzeug.security import check_password_hash

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profiles')
def profiles():
    """Render the all profiles in database"""
    files = get_uploaded_images()
    users = db.session.query(UserProfile).all()
    return render_template('profiles.html', files=files, users =users)
    
@app.route('/profile/<userid>')
def userprofile(userid):
    """Render the profile of requested user in database"""
    files = get_uploaded_images()
    user = UserProfile.query.filter_by(id=userid).first()
    return render_template('userprofile.html', files=files, user=user)
    
    
@app.route('/profile', methods=['POST',"GET"])
def profile():
    # Instantiate your form class
    form = UploadForm()

    # Validate file upload on submit
    if request.method == 'POST':
        # Get file data and save to your uploads folder
        if form.validate_on_submit():
            user = UserProfile(request.form['firstname'],request.form['lastname'],request.form['email'],request.form['location'],request.form['gender'],request.form['bio'])
            db.session.add(user)
            db.session.commit()
            files = request.files['image']
            filename = secure_filename(files.filename)
            files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('New user was successfully added')
            return redirect(url_for('profiles'))

    return render_template('upload.html', form = form)

def get_uploaded_images():
	rootdir = os.getcwd()
	dirs = []
	for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads'):
		for file in files:
			if("gitkeep" not in os.path.join(subdir, file)):
				dirs.append(file) 
	return dirs 


###
# The functions below should be applicable to all Flask apps.
###
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
