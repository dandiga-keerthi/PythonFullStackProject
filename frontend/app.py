import streamlit as st
import sys
import os

# Add src to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.db import create_user, get_user_by_email, update_user_stats, get_leaderboard
from src.logic import generate_event, resolve_event

# --- Page config ---
st.set_page_config(page_title="Micro-Decision RPG", layout="wide")
st.title("🛡️ Micro-Decision RPG Adventure")

# --- Session state setup ---
if "user" not in st.session_state:
    st.session_state.user = None
if "event" not in st.session_state:
    st.session_state.event = None
if "message" not in st.session_state:
    st.session_state.message = ""
if "refresh" not in st.session_state:
    st.session_state.refresh = False  # Used to trigger refresh

# --- Login / Signup ---
st.sidebar.header("Login / Signup")
email = st.sidebar.text_input("Email")
username = st.sidebar.text_input("Username (if new)")

if st.sidebar.button("Login / Signup"):
    user = get_user_by_email(email)
    if not user and username:
        create_user(username, email)
        user = get_user_by_email(email)
        st.success(f"User created: {username}")
    elif user:
        st.success(f"Welcome back {user['username']}")
    else:
        st.warning("Enter a username to sign up")
    st.session_state.user = user
    st.session_state.event = generate_event()

# --- Main game ---
if st.session_state.user:

    # Refresh user stats from DB
    user = get_user_by_email(st.session_state.user['email'])
    st.session_state.user = user

    # Sidebar stats
    st.sidebar.subheader("Player Stats")
    st.sidebar.write(f"HP: {user['hp']}")
    st.sidebar.write(f"Gold: {user['gold']}")
    st.sidebar.write(f"XP: {user['xp']}")
    st.sidebar.write(f"Inventory: {user.get('inventory', [])}")

    # Generate new event if none exists
    if st.session_state.event is None:
        st.session_state.event = generate_event()

    st.subheader("Adventure Event")
    st.write(st.session_state.event['description'])

    # Display choices as buttons
    cols = st.columns(len(st.session_state.event['choices']))
    for idx, choice in enumerate(st.session_state.event['choices']):
        if cols[idx].button(choice):
            result = resolve_event(user, choice, st.session_state.event)
            st.session_state.message = result['message']

            # Update user stats in Supabase
            update_user_stats(user['id'], result['hp'], result['gold'], result['xp'], result['inventory'])

            # Generate new event
            st.session_state.event = generate_event()

            # Trigger a refresh
            st.session_state.refresh = not st.session_state.refresh

    # Show event outcome message
    if st.session_state.message:
        st.success(st.session_state.message)

    # --- Leaderboard ---
    st.subheader("🏆 Leaderboard")
    leaderboard = get_leaderboard()
    for i, player in enumerate(leaderboard, 1):
        st.write(f"{i}. {player['username']} - XP: {player['xp']} | Gold: {player['gold']}")

else:
    st.info("Please login to start your adventure!")
