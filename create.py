from application.main import app, db

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

# Charge en même temps les données de data.sql

with open("data.sql") as f:
    import sqlite3
    conn = sqlite3.connect(app.config.get("SQLALCHEMY_DATABASE_URI").replace("sqlite:///", ""))
    conn.executescript(f.read().strip())
    conn.commit()
