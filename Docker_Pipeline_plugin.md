### Docker Pipeline

Using the GUI: From your Jenkins dashboard navigate to Manage Jenkins > Manage Plugins and select the Available tab. Locate this plugin by searching for docker-workflow.
Using the CLI tool:
jenkins-plugin-cli --plugins docker-workflow:572.v950f58993843
Using direct upload. Download one of the releases and upload it to your Jenkins instance.

### System configure
sudo gpasswd -a jenkins docker
sudo service docker restart
sudo systemctl restart jenkins

### Docker agent

mkdir ctx # empty directory
docker build -t jenkins_agent -f Dockerfile ctx

### test Connect

docker run -i -t jenkins_agent bash

### REMOVE  

To delete all containers including its volumes use,

docker rm -vf $(docker ps -aq)


To delete all the images,

docker rmi -f $(docker images -aq)
Remember, you should remove all the containers before removing all the images from which those containers were created.
