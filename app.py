import streamlit as st
import time
import random

# Page config
st.set_page_config(page_title="MiniCraft v2", page_icon="⛏️", layout="centered")

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #1e1e1e;
        color: #f0f0f0;
    }
    .stTextInput>div>div>input {
        background-color: #2d2d2d;
        color: white;
        border: 2px solid #555;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        border: 2px solid #388E3C;
        transition: 0.2s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        border-color: #2E7D32;
    }
    
    .card {
        background-color: #2d2d2d;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin-bottom: 10px;
        text-align: center;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .card-title {
        font-size: 14px;
        color: #aaaaaa;
        margin-bottom: 5px;
    }
    .card-value {
        font-size: 24px;
        font-weight: bold;
    }
    
    .rarity-common { border-left-color: #9e9e9e; }
    .rarity-uncommon { border-left-color: #4CAF50; }
    .rarity-rare { border-left-color: #2196F3; }
    .rarity-epic { border-left-color: #9C27B0; }
    .rarity-legendary { border-left-color: #FFC107; }
</style>
""", unsafe_allow_html=True)

# Game Data
common = ["DIRT", "SAND", "WOOD", "GRAVEL", "CLAY", "SNOW"]
uncommon = ["IRON", "COPPER", "REDSTONE", "QUARTZ"]
rare = ["GOLD", "DIAMOND", "EMERALD", "OBSIDIAN"]
epic = ["DRAGON EGG", "NETHER STAR", "ELYTRA"]

# Initialize Session State
if "words_mined" not in st.session_state:
    st.session_state.words_mined = 0
if "legendary_finds" not in st.session_state:
    st.session_state.legendary_finds = 0
if "letter_counts" not in st.session_state:
    st.session_state.letter_counts = {}

# Functions from original logic
def vowel_check(word):
    return sum(1 for i in word.lower() if i in "aeiou")

def consonants_check(word):
    return sum(1 for j in word.lower() if j.isalpha() and j not in "aeiou")

def info_collect(word):
    freq = {}
    for u in word.lower():
        if u.isalpha():
            freq[u] = freq.get(u, 0) + 1
    return freq

def uniqueness(word):
    freq = info_collect(word)
    return sum(1 for l in freq if freq[l] == 1)

def get_rarity(unique_count, length):
    if unique_count > 7 and length >= 10:
        return "Epic", random.choice(epic), "rarity-epic"
    elif unique_count > 5:
        return "Rare", random.choice(rare), "rarity-rare"
    elif unique_count >= 3:
        return "Uncommon", random.choice(uncommon), "rarity-uncommon"
    else:
        return "Common", random.choice(common), "rarity-common"

# UI Header
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h1 style="color: #4CAF50; text-shadow: 2px 2px #2E7D32;">⛏️ MiniCraft</h1>
    <h3 style="color: #aaaaaa;">Word Resource Finder</h3>
</div>
""", unsafe_allow_html=True)

# Sidebar Inventory
st.sidebar.title("📚 Inventory")
st.sidebar.metric("Words Mined", st.session_state.words_mined)
st.sidebar.metric("Epic Finds", st.session_state.legendary_finds)

if st.session_state.letter_counts:
    most_common = max(st.session_state.letter_counts, key=st.session_state.letter_counts.get)
    st.sidebar.markdown(f"**Most Common Letter:** {most_common.upper()}")
else:
    st.sidebar.markdown("**Most Common Letter:** None")

# Main Interface
block = st.text_input("📝 Enter a word to mine:", placeholder="e.g. Minecraft")

if st.button("⛏️ Mine Word!", use_container_width=True):
    if not block.strip():
        st.warning("Please enter a valid word!")
    else:
        # Mining Animation
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            time.sleep(0.015)
            progress_bar.progress(i + 1)
            if i % 25 == 0:
                status_text.text(["Swinging pickaxe...", "Breaking block...", "Unraveling mysteries...", "Almost there..."][i//25])
        
        status_text.empty()
        progress_bar.empty()
        st.success("✨ Mining Complete!")
        
        # Calculate stats
        word_length = len(block)
        vowels = vowel_check(block)
        consonants = consonants_check(block)
        unique_letters = uniqueness(block)
        rarity_level, resource_found, rarity_class = get_rarity(unique_letters, word_length)
        
        # Update session state
        st.session_state.words_mined += 1
        if rarity_level == "Epic":
            st.session_state.legendary_finds += 1
            st.balloons()
        elif rarity_level == "Rare":
            st.snow()
            
        freq = info_collect(block)
        for char, count in freq.items():
            st.session_state.letter_counts[char] = st.session_state.letter_counts.get(char, 0) + count
        
        st.markdown("---")
        st.subheader("💎 Resources Found")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Vowel Crystals</div>
                <div class="card-value">✨ {vowels}</div>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Consonant Fragments</div>
                <div class="card-value">🪨 {consonants}</div>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Hidden Runes</div>
                <div class="card-value">🌟 {unique_letters}</div>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("---")
        st.subheader("🎁 Loot Chest")
        
        # The Loot Card
        resource_emoji = "🟫" if rarity_level == "Common" else "⬜" if rarity_level == "Uncommon" else "💎" if rarity_level == "Rare" else "🐉"
        
        st.markdown(f"""
        <div class="card {rarity_class}" style="max-width: 300px; margin: auto;">
            <div class="card-title">{rarity_level} Find!</div>
            <div class="card-value" style="font-size: 32px;">{resource_emoji} {resource_found}</div>
        </div>
        """, unsafe_allow_html=True)
