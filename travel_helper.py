import random
from difflib import SequenceMatcher

# Travel destination database
TRAVEL_DATABASE = {
    "paris": {
        "country": "France",
        "best_time": "April to June, September to October",
        "attractions": ["Eiffel Tower", "Louvre Museum", "Notre-Dame Cathedral", "Arc de Triomphe", "Sacré-Cœur"],
        "food": ["Croissants", "French Onion Soup", "Crêpes", "Cheese and Wine", "Macarons"],
        "budget": "$150-300 per day",
        "language": "French",
        "currency": "Euro",
        "description": "The City of Light, known for its romantic ambiance, world-class museums, and exquisite cuisine."
    },
    "tokyo": {
        "country": "Japan",
        "best_time": "March to May, September to November",
        "attractions": ["Tokyo Tower", "Senso-ji Temple", "Shibuya Crossing", "Meiji Shrine", "Tsukiji Market"],
        "food": ["Sushi", "Ramen", "Tempura", "Takoyaki", "Okonomiyaki"],
        "budget": "$100-250 per day",
        "language": "Japanese",
        "currency": "Japanese Yen",
        "description": "A vibrant metropolis blending ancient traditions with cutting-edge technology and innovation."
    },
    "new york": {
        "country": "USA",
        "best_time": "April to June, September to November",
        "attractions": ["Statue of Liberty", "Central Park", "Times Square", "Empire State Building", "The Met"],
        "food": ["Hot Dogs", "Pizza", "Bagels", "Hamburgers", "New York Cheesecake"],
        "budget": "$200-400 per day",
        "language": "English",
        "currency": "US Dollar",
        "description": "The city that never sleeps, offering world-class entertainment, dining, and iconic landmarks."
    },
    "bangkok": {
        "country": "Thailand",
        "best_time": "November to February",
        "attractions": ["Grand Palace", "Wat Phra Kaew", "Floating Markets", "Chao Phraya River", "Jim Thompson House"],
        "food": ["Pad Thai", "Tom Yum", "Green Curry", "Mango Sticky Rice", "Satay"],
        "budget": "$50-150 per day",
        "language": "Thai",
        "currency": "Thai Baht",
        "description": "Thailand's bustling capital known for its ornate shrines, vibrant street life, and delicious cuisine."
    },
    "london": {
        "country": "United Kingdom",
        "best_time": "May to September",
        "attractions": ["Big Ben", "Tower of London", "British Museum", "Buckingham Palace", "Tower Bridge"],
        "food": ["Fish and Chips", "Sunday Roast", "Afternoon Tea", "Bangers and Mash", "Sticky Toffee Pudding"],
        "budget": "$150-300 per day",
        "language": "English",
        "currency": "British Pound",
        "description": "A historic city blending royal heritage with modern culture, museums, and world-famous landmarks."
    },
    "dubai": {
        "country": "United Arab Emirates",
        "best_time": "November to March",
        "attractions": ["Burj Khalifa", "Palm Jumeirah", "Dubai Mall", "Gold Souk", "Desert Safari"],
        "food": ["Shawarma", "Hummus", "Falafel", "Biryani", "Dates"],
        "budget": "$200-350 per day",
        "language": "Arabic, English",
        "currency": "UAE Dirham",
        "description": "A luxurious desert city known for modern architecture, shopping, and unique desert experiences."
    }
}


def find_destination(user_input):
    """Find destination using fuzzy matching"""
    user_input = user_input.lower().strip()
    
    # Direct match
    if user_input in TRAVEL_DATABASE:
        return user_input
    
    # Fuzzy matching
    best_match = None
    best_ratio = 0
    
    for destination in TRAVEL_DATABASE.keys():
        ratio = SequenceMatcher(None, user_input, destination).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = destination
    
    if best_ratio > 0.6:
        return best_match
    
    return None


def search_destinations(query):
    """Search for destinations matching the query"""
    query_lower = query.lower().strip()
    results = []
    
    for destination in TRAVEL_DATABASE.keys():
        if query_lower in destination or destination in query_lower:
            results.append(destination)
    
    if not results:
        match = find_destination(query)
        if match:
            results.append(match)
    
    return results


def get_destination_info(destination):
    """Get formatted information about a destination"""
    destination_key = find_destination(destination)
    
    if not destination_key or destination_key not in TRAVEL_DATABASE:
        return None
    
    info = TRAVEL_DATABASE[destination_key]
    
    response = f"""
## 🌍 {destination_key.upper()} - {info['country']}

**{info['description']}**

### 📍 Basic Information
- **Country**: {info['country']}
- **Language**: {info['language']}
- **Currency**: {info['currency']}
- **Average Daily Budget**: {info['budget']}

### ⏰ Best Time to Visit
{info['best_time']}

### 🏛️ Top Attractions
"""
    
    for attraction in info['attractions']:
        response += f"- {attraction}\n"
    
    response += "\n### 🍽️ Must-Try Foods\n"
    for food in info['food']:
        response += f"- {food}\n"
    
    return response


def get_travel_tips():
    """Get random travel tips"""
    tips = [
        "🎒 **Pack Light** - You'll appreciate it when carrying luggage through airports and streets!",
        "💳 **Carry Cash** - Not all places accept cards everywhere, especially in local markets.",
        "📱 **Get Connected** - Buy a local SIM card or activate an international plan for staying connected.",
        "🗺️ **Download Offline Maps** - Use Google Maps offline before traveling to remote areas.",
        "🚗 **Learn Basic Phrases** - Learn key phrases in the local language for better interactions.",
        "🏥 **Check Requirements** - Verify travel insurance, visas, and vaccination requirements.",
        "📸 **Respect Culture** - Always ask permission before taking photos of locals and respect local customs.",
        "🕐 **Account for Time Zones** - Calculate time differences to manage jet lag better.",
        "🍽️ **Try Street Food** - Local street food offers authentic experiences and great value.",
        "🏨 **Book in Advance** - Reserve accommodations early, especially during peak seasons.",
        "💰 **Use ATMs** - Withdraw money from ATMs instead of exchanging at airports for better rates.",
        "✈️ **Flexible Dates** - Flying on weekdays is usually cheaper than weekends.",
        "🎫 **Buy City Passes** - Get tourist passes for free or discounted museum entries.",
        "👥 **Join Tours** - Group tours help you meet other travelers and learn more about destinations.",
        "🧳 **Travel Insurance** - Always get comprehensive travel insurance for peace of mind."
    ]
    
    selected_tips = random.sample(tips, 7)
    tips_text = "## 🎒 Travel Tips for You\n\n"
    for tip in selected_tips:
        tips_text += f"- {tip}\n"
    
    return tips_text


def get_budget_comparison(destinations_list):
    """Compare budgets between destinations"""
    if not destinations_list:
        return "❌ Please specify destinations to compare!"
    
    response = "## 💰 Budget Comparison\n\n"
    response += "| Destination | Budget per Day | Country |\n"
    response += "|---|---|---|\n"
    
    found_any = False
    for dest in destinations_list:
        dest_key = find_destination(dest)
        if dest_key and dest_key in TRAVEL_DATABASE:
            budget = TRAVEL_DATABASE[dest_key]['budget']
            country = TRAVEL_DATABASE[dest_key]['country']
            response += f"| {dest_key.capitalize()} | {budget} | {country} |\n"
            found_any = True
        else:
            response += f"| {dest} | ❌ Not found | - |\n"
    
    if not found_any:
        return "❌ No valid destinations found for comparison!"
    
    return response


def get_all_destinations():
    """Get list of all available destinations"""
    return list(TRAVEL_DATABASE.keys())
