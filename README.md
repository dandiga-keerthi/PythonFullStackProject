Micro-Decision RPG

## Introduction

Micro-Decision RPG is a decision-based adventure game where players navigate a series of events by making strategic choices. The game uses Python for backend logic, Supabase for database management, and Streamlit for the frontend. Player progress, stats, and inventory are stored persistently in Supabase.
The game focuses on choices and consequences, with an evolving story and player stats influenced by each decision.

## Features
- Turn-based decision-making gameplay
- Dynamic events with multiple choice outcomes
- Player stats tracking: HP, Gold, XP, Inventory
- Persistent player progress saved in Supabase
- Leaderboard showing top players by XP or Gold
- Web-based frontend interface using Streamlit
- Backend powered by Python logic and optional FastAPI endpoints

## Project Structure

MicroDecisionRPG/
├── src/                  # Core game logic and database interaction
│   ├── logic.py          # Event generation, choice resolution, stat calculations
│   ├── db.py             # Supabase database interface (CRUD operations for users, stats)
│   └── utils.py          # Helper functions: random events, color validation, etc.
├── frontend/             # Frontend app assets
│   ├── app.py            # Streamlit frontend server
│   ├── static/           # CSS, JS, images for frontend (optional)
│   └── templates/        # HTML templates (if using Flask-like rendering)
├── api/                  # Optional backend API
│   └── main.py           # FastAPI entry point serving game events or stats
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables (Supabase credentials)
└── .gitignore            # Git ignore rules

## Requirements

Python 3.8 or higher
Supabase account and project setup
Python packages listed in requirements.txt
Modern web browser to run the Streamlit

## Installation

1. Clone or Download the Project

Option 1: Clone with Git
git clone <repository_url>

Option 2: Download ZIP

Extract to a folder.

2. Install Python Dependencies

pip install -r requirements.txt

3. Set up Supabase Database

-Create a Supabase project.

-Create the users table:

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    hp INT DEFAULT 100,
    gold INT DEFAULT 0,
    xp INT DEFAULT 0,
    inventory JSONB DEFAULT '[]',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-Optionally, create additional tables for leaderboard or events.

4. Configure Environment Variables

-Create a .env file in the project root:
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key

5. Run the Application

-Streamlit Frontend

cd frontend
streamlit run app.py

Opens in browser at http://localhost:8501

-FastAPI Backend (Optional)

cd api
uvicorn main:app --reload

API available at http://localhost:8000

## How to Play

1. Login or Signup using an email and username.

2. Make choices in each event to affect your stats: HP, Gold, XP, Inventory.

3. Player stats are displayed in the sidebar.

4. Leaderboard shows top players based on XP or Gold.

5. Each choice triggers an event resolution and updates the database.

## Technical Details

## Technologies Used

- Frontend: Streamlit (Python)

- Backend: Python logic, optional FastAPI API endpoints

- Database: Supabase (PostgreSQL-based)

- Language: Python 3.8+

## Key Components

- **`frontend/app.py`** → Streamlit UI and player interaction

- **`src/logic.py`** → Event generation, outcome resolution, stat updates

- **`src/db.py`** → CRUD operations with Supabase

- **`src/utils.py`** → Helper functions (randomization, validation)

- **`api/main.py`** → Optional API for fetching events or stats

## Troubleshooting

1. Module import errors: Ensure pip install -r requirements.txt is run and Python path is correct.
2. Supabase connection issues: Check .env for correct URL and API key.
3. Stats not updating: Verify database writes succeed in Supabase.
4. Leaderboard not showing correctly: Ensure query sorts by XP/Gold correctly.

## Future Enhancements

- Add more complex events and branching storylines.

- Implement real-time multiplayer events using Supabase Realtime.

- Add visual styling and graphics to events.

- Create achievements, quests, and special items.

- Integrate sound effects or simple animations in Streamlit.

## Support

Report issues or request features on the GitHub Issues page.

Contact the maintainer at: keerthi.dandiga17@gmail.com