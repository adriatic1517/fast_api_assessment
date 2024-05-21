Install Docker.

Run postgres with `docker compose up -d`. This will start a postgres container and expose it on `localhost:5432`.

Activate virtual env `source env/bin/activate`, `pip install -r requirements.txt` and run with `fastapi dev main.py`

Access lead form at `localhost:8000` to send email with `emadalma40@gmail.com`

See all leads at `localhost:8000/leads`
