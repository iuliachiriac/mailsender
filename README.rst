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

    # Follow instructions in instance/settings.py to adapt it to your needs.
