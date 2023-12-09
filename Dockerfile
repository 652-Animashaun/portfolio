FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN apt-get update && apt-get install vim -y
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 5000
RUN echo 'export PS1="\[\e[36m\]zappashell>\[\e[m\]"' >> /root/.bashrc
CMD ["bash"]
