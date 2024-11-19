install:
	@echo "Installing dependencies..."
	python -m pip install -r requirements.txt

add:
	@echo "Installing a new package..."
	python -m pip install $(package) && python -m pip freeze > requirements.txt

run-server:
	@echo "Running the server..."
	python ./schedule_generator/manage.py runserver 0.0.0.0:8000

migrate:
	@echo "Migrating the database..."
	python ./schedule_generator/manage.py migrate 

new-migration:
	@echo "Creating a new migration..."
	python ./schedule_generator/manage.py makemigrations

run-fixtures:
	@echo "Running fixtures..."
	python ./schedule_generator/manage.py migrate && \
	python ./schedule_generator/manage.py loaddata ./schedule_generator/fixtures/*.json

new-app:
	cd ./schedule_generator && python manage.py startapp $(name)

db-reset:
	docker-compose exec db mysql -uroot -p -e "DROP DATABASE schedule_generator; CREATE DATABASE schedule_generator;"

add-app:
	@read -p "Enter new item: " item; \
	cd ./schedule_generator/schedule_generator && python modify_array.py $$item

