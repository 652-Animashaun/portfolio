docker run -ti -e AWS_PROFILE=zappa_user -p 5000:5000 -v "$(pwd):/app/" -v ~/.aws:/root/.aws --rm personal_blog