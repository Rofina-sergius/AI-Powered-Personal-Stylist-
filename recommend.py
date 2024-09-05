# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 19:36:05 2024

@author: DELL
"""

def recommend(skin_tone, body_type):
    clothing_recommendations = {
        "light": {
            "Tall and Slim": ["Dark suits", "Vertical stripes"],
            "Average": ["Pastel colors", "Blazers"],
            "Short and Broad": ["V-neck tops", "Solid colors"]
        },
        "medium": {
            "Tall and Slim": ["Bold colors", "Layers"],
            "Average": ["Earth tones", "Tailored fits"],
            "Short and Broad": ["Monochrome outfits", "Patterns"]
        },
        "dark": {
            "Tall and Slim": ["Light colors", "Horizontal stripes"],
            "Average": ["Bright colors", "Denim"],
            "Short and Broad": ["Bold patterns", "Light tops"]
        }
    }
    accessories_recommendations = {
        "light": ["Silver jewelry", "Bright scarves"],
        "medium": ["Gold jewelry", "Leather belts"],
        "dark": ["Colorful ties", "Statement necklaces"]
    }
    
    skin_tone_category = "medium"
    if skin_tone[0] < 15:
        skin_tone_category = "dark"
    elif skin_tone[0] > 35:
        skin_tone_category = "light"
    
    clothing = clothing_recommendations[skin_tone_category][body_type]
    accessories = accessories_recommendations[skin_tone_category]
    
    return clothing, accessories

if __name__ == "__main__":
    # Example usage
    skin_tone = [30, 40, 50]  # Example HSV values
    body_type = "Average"
    clothing, accessories = recommend_clothing_and_accessories(skin_tone, body_type)
    print("Recommended Clothing:", clothing)
    print("Recommended Accessories:", accessories)
