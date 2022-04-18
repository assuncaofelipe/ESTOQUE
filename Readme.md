# :books: Readme - Project of Software Engineer II

Sistema de Estoque para cadastro de produtos
Equipe:
- Felipe V Assunção
- Thiago Rodrigues
- Edson Júnior
- José Anderson

## Instalation and Execution
Step 1: Creation of virtual environments (venv)
	
		```python -m venv venv```

Step 2: Run venv from terminal 

	Access the directories: 
		```cd .\venv\Scripts\ ```
		
	Run: 
		```.\activate```

Step 4: installing dependencies (it is necessary that the venv will be running)

	Access the project root directory with venv running and execute: 
	
		```pip install django django-bootstrap-v5 django-bootstrap-form ```

		```pip install asgiref certifi chardet  ```

		```pip install idna pytz requests sqlparse urllib3 ```
	
	
	All dependencies are in ```requirements.txt``` file 
	

Step 5: Run the project (it is necessary that the venv will be running)

	Run in project root with venv running (use terminal)
	
		```python manage.py runserver```
