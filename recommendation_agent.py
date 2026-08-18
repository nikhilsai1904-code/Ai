# recommendation_agent.py

import random

# Sample fictional Reels dataset
sample_reels = [
    {"id": 1, "title": "Funny Java Meme", "category": "Entertainment/Programming"},
    {"id": 2, "title": "Gaming Highlight Reel", "category": "Gaming"},
    {"id": 3, "title": "AI News Snippet", "category": "AI/Tech News"},
    {"id": 4, "title": "Laptop Comparison", "category": "Hardware"},
    {"id": 5, "title": "Coding Interview Joke", "category": "Career/Programming"},
    {"id": 6, "title": "Software Engineer Lifestyle Reel", "category": "Career"},
    {"id": 7, "title": "Programming Meme (Python)", "category": "Entertainment/Programming"},
    {"id": 8, "title": "Tech Career Advice Clip", "category": "Career"}
]

# Mapping broader interests
interest_map = {
    "Entertainment/Programming": "Software Engineering Career",
    "Gaming": "Tech + Gaming Hardware",
    "AI/Tech News": "Artificial Intelligence",
    "Hardware": "Computer Hardware & Gadgets",
    "Career/Programming": "Interview Preparation & DSA",
    "Career": "Software Engineering Career"
}

# Recommendations database
recommendations = {
    "Software Engineering Career": {
        "title": "Top 5 DSA Concepts for Coding Interviews",
        "category": "DSA / Career",
        "difficulty": "Intermediate"
    },
    "Tech + Gaming Hardware": {
        "title": "Best Budget GPUs for Students",
        "category": "Hardware",
        "difficulty": "Beginner"
    },
    "Artificial Intelligence": {
        "title": "Intro to Neural Networks Explained Simply",
        "category": "AI",
        "difficulty": "Beginner"
    },
    "Computer Hardware & Gadgets": {
        "title": "How to Choose the Right Laptop for Coding",
        "category": "Hardware",
        "difficulty": "Beginner"
    },
    "Interview Preparation & DSA": {
        "title": "Dynamic Programming Made Easy",
        "category": "DSA",
        "difficulty": "Intermediate"
    }
}

def analyze_reel(reel):
    current_reel = reel["title"]
    interest_detected = interest_map.get(reel["category"], "General Tech")
    recommendation = recommendations.get(interest_detected, {
        "title": "Latest Tech Trends for Students",
        "category": "Other",
        "difficulty": "Beginner"
    })

    output = {
        "CURRENT REEL": current_reel,
        "INTEREST DETECTED": interest_detected,
        "WHY": f"Based on category '{reel['category']}' and broader context.",
        "RECOMMENDED TECH REEL": recommendation["title"],
        "CATEGORY": recommendation["category"],
        "WHY THIS RECOMMENDATION": f"Connects to {interest_detected} interest.",
        "DIFFICULTY": recommendation["difficulty"],
        "CONFIDENCE": "High"
    }
    return output


# Demo run
if __name__ == "__main__":
    for reel in sample_reels:
        result = analyze_reel(reel)
        print("\n--- Recommendation ---")
        for k, v in result.items():
            print(f"{k}: {v}")
