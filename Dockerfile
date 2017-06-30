FROM alpine:3.5

# Install python and pip
RUN apk add --update py2-pip

# upgrade pip
RUN pip install --upgrade pip

# install Python modules needed by the Python app
COPY requirements.txt /taas/requirements.txt
RUN pip install --no-cache-dir -r /taas/requirements.txt

# copy over and run the app
COPY . /taas
ENV FLASK_APP /taas/taas/app.py
CMD ["flask", "run"]
