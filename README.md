# Step by Step

- [X] Project initial configuration: pre-commits, linters, .venv, etc;
- [X] Setting up the initial project structure: folders and files;
- [X] Creating initial FastAPI app with sanity endoint;
- [X] Create entities: Users and Repos;
- [X] Create repositories: Abstract and Users;
- [X] Implements the github api integration;
- [X] Create controller: User (backend first), three endpoints: `GET /`, `POST /`, `GET /{username}`;
- [X] Include the controller in the app;
- [X] Set up mongo with docker-compose;
- [X] Implement use of templates;
- [X] Create templates;
- [X] Include celery for periodic tasks;
- [X] Write documentation for running the project;
- [ ] Add pytest routine to pre-commit;
- [ ] Test entities;
- [ ] Test repositories;
- [ ] Test controllers;
- [ ] Test github api integration;
- [ ] Complete documentation: running the tests;
- [ ] Styling templates;
- [ ] Configure workflows;

---

# Running the project

- Clone the project;

- Use docker compose to raise mongo container;

```bash
docker compose up -d
```

- Create a virtual environment;

```bash
python3 -m venv .venv
```

- Activate the virtual environment;

```bash
source .venv/bin/activate
```

- Install the dependencies;

```bash
pip install -r requirements.txt
```

- Run Fastapi application;

```bash
uvicorn src.app:app --reload
```

- Access the application on the browser: [http://localhost:8000](http://localhost:8000)

- Have fun!

- If you want to activate periodic tasks, run rabbitmq container;

```bash
docker run -d -p 5672:5672 rabbitmq
```

- Run celery worker;

```bash
celery -A src.celery worker -l info
```

- Run celery beat;

```bash
celery -A src.celery beat -l info
```

- Tasks will be executed every 30 seconds for proof of concept;

--- 
