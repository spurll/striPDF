from os import path, listdir
from io import BytesIO
from tempfile import TemporaryFile, mkstemp
from string import ascii_letters, digits, punctuation
from random import choice
from flask import render_template, flash, session, send_file
from flask_wtf import FlaskForm
from wtforms.fields import FileField
from wtforms.validators import DataRequired, ValidationError
from pikepdf import Pdf

from stripdf import app


TEMP_DIR = app.config.get('TEMP_DIR')


class UploadForm(FlaskForm):
    file_field = FileField(validators=[DataRequired()])


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if form.is_submitted():
        if form.validate_on_submit():
            try:
                filename=form.file_field.data.filename

                with TemporaryFile(dir=TEMP_DIR) as uploaded:
                    form.file_field.data.save(uploaded)

                    converted, converted_path = mkstemp(dir=TEMP_DIR)

                    with Pdf.open(uploaded) as pdf:
                        pdf.save(converted_path)

                    return send_file(converted_path,
                        as_attachment=True,
                        download_name=filename,
                        mimetype='application/pdf')

            except Exception as e:
                flash('An error occurred: {}'.format(e))

        else:
            flash_errors(form)

    return render_template('index.html', form=form)


def flash_errors(form):
    for field, messages in form.errors.items():
        label = getattr(getattr(getattr(form, field), 'label'), 'text', '')
        label = label.replace(':', '')
        error = ', '.join(messages)

        message = f'Error in {label}: {error}' if label else 'Error: {error}'

        flash(message)
        print(message)
