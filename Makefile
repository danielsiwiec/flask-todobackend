run:
	FLASK_APP=todo.py pipenv run flask run

docker:
	docker build . -t flask-todo && docker run -p 5000:5000 flask-todo