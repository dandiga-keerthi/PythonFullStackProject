from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def create_user(username, email):
    supabase.table("users").insert({"username": username, "email": email, "hp": 100, "gold": 0, "xp": 0, "inventory": []}).execute()

def get_user_by_email(email):
    user = supabase.table("users").select("*").eq("email", email).execute()
    return user.data[0] if user.data else None

def update_user_stats(user_id, hp, gold, xp, inventory):
    supabase.table("users").update({
        "hp": hp,
        "gold": gold,
        "xp": xp,
        "inventory": inventory
    }).eq("id", user_id).execute()

def get_leaderboard(limit=10):
    result = supabase.table("users").select("*").order("xp", desc=True).limit(limit).execute()
    return result.data
