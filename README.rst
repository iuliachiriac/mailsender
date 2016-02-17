Mail Sender
===========

.. contents ::

Project Name
------------
The Project Name is Mail Sender.

Description
-----------
This is a very simple application used to send individual e-mails using
 different templates to multiple persons based on a CSV input file.

Installation
------------
We should use Virtualenv for isolated environments. The following commands will
be run as an unprivileged user::

1. Clone the repository::

    git clone https://github.com/iuliachiriac/mailsender.git
    cd mailsender

2. Create & activate a virtual environment::

    virtualenv sandbox
    echo '*' > sandbox/.gitignore
    source sandbox/bin/activate

3. Install dependencies::

    pip install -r requirements.txt

4. Create a configuration file::

    mkdir -p instance
    cp settings.py.example instance/settings.py

Usage
-----

1. You should store your recipients in a CSV file that has the following
   fields: score, name and e-mail. Store these fields' names in the
   corresponding settings variables (SCORE_FIELD, NAME_FIELD, MAIL_FIELD).

2. Write your e-mail templates, similar to `example.html`.

3. Map the e-mail templates to the scores and store them in the
   SCORE_HTML_MAPPING variable.

4. Run the management command that gets the actual work done::

    python manage.py send_mails -f the_name_of_your_recipients_file.csv
