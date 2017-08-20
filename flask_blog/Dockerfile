
#Pull base image
FROM centos:7.0.1406

# build commands
RUN yum install -y python-setuptools mysql-connector-python mysql-devel gcc python-devel --skip-broken
RUN easy_install pip
RUN mkdir /opt/flask_blog
WORKDIR /opt/flask_blog

ADD requirements.txt /opt/flask_blog/
RUN pip install -r requirements.txt
# RUN rm -rf ./migrations
ADD . /opt/flask_blog



# CMD ["python", "manage.py", "db", "init"]
# CMD ["python", "manage.py", "db", "migrate"]
# CMD ["python", "manage.py", "db", "upgrade"]

# CMD ["python", "manage.py", "runserver"]


