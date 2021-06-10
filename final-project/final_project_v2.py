"""
This program provides the user with a suggestion of a food or drink of Asian or Pacific Islander origin
to help in celebrating Asian American and Pacific Islander Heritage Month.
The program initializes a database with 31 options and randomly selects one to show the user.
The program will provide a suggestion with a short description of the food/drink.
The user has the opportunity to ask for multiple suggestions. 
The user can also suggest additional food/drinks to be added to our list.
"""

import random

def main():
    eat = create_eat()
    another_response = True
    has_suggestion = True

    print("Happy Asian American and Pacific Islander Heritage Month!")
    print("Celebrate by eating or drinking something with an Asian or Pacific Islander origin each day!")

    while another_response:
        response = get(eat) 
        print_response(response)
        another_response = another()
    while has_suggestion:
        has_suggestion = suggestion()
        if has_suggestion:
            new_suggestion(eat)
        else:
            show_all_suggestions = input("Would you like to see all the suggestions (y/n)? ")
            if show_all_suggestions == 'y':
                for i in range(len(eat)):
                    print_response(eat[i])
            print("\nCome back for another suggestion on how to celebrate AAPIHM tomorrow!\n")


def suggestion():
    is_suggestion = input('\nDo you have a suggestion of a food/drink to celebrate AAPIHM (y/n)? ')
    new_suggestion = {}
    if is_suggestion == 'n':
        return False
    else:
        return True

def new_suggestion(eat):
    suggestion = {}
    suggestion['name'] = input('\nWhat food/drink do you suggest? ')
    suggestion['description'] = input('Please describe this food/drink: ')
    action = "eating/drinking " + str(suggestion['name'])
    suggestion['action'] = action
    eat.append(suggestion)
    print("Thank you for that suggestion! We will add it to our list.")

def another():
    another = input('\nWould you like another suggestion (y/n)? ')
    if another == 'y':
        return True
    else:
        return False

def get(eat):
    i = random.randint(0, len(eat) -1)
    response = eat[i]
    return response

def print_response(response):
    print("\nYou can celebrate by " + response['action'] + ".")
    print(response['description'])

def create_eat():
    """
    initialize list of dictionaries options to celebrate with eating/drinking
    """
    eat = [
        {"name":"bubble tea/boba", "description": "Bubble tea is a tea-based drink from Taiwan that consists of tea and chewy tapioca balls called boba.", "action": "drinking your favorite bubble tea/boba"},
        {"name": "dumplings", "description": "several Asian cuisines include dumplings that can be boiled, pan-fried, or steamed and can include meat and veggies on the inside.", "action": "eating at your favorite dumpling spot"},
        {"name": "sushi", "description": "Sushi is a Japanese dish with seaweed wrapped around rice and vegetables and/or seafood.", "action": "eating some sushi"},
        {"name": "ramen", "description": "Ramen is a Japanese noodle soup dish that is often served in a pork broth with sliced pork, nori, scallions, and wheat noodles.", "action": "eating ramen"},
        {"name": "Pad Thai", "description": "Pad Thai is a stir-fried rice noodle dish with rice noodles, protein, peanuts, scrambled eggs, and bean sprouts.", "action": "eating Pad Thai"},
        {"name": "Bahn Mi", "description": "Bahn mi is a Vietnamese sandwich on a baguette with a fusion of meats and vegetables, often including a protein, cilantro, cucumber, carrots, pickled daikon, chili, and mayo.", "action": "eating a bahn mi"},
        {"name": "Pho", "description": "Pho is a Vietnamese noodle soup dish consisting of broth, rice noodles, herbs, and meat.", "action": "eating pho"},
        {"name": "Indian curry", "description": "Indian curries often include vegetables or a protein cooked in a curry sauce that can include a combination of spices often including tumeric, cumin, coriander, ginger, and chilies.", "action": "eating Indian curry"},
        {"name": "beef noodle soup", "description": "Beef noodle soup is a Chinese noodle soup dish made of stewed braised beef, beef broth, vegetables, and noodles.", "action": "eating beef noodle soup"},
        {"name": "Korean BBQ", "description": "Korean BBQ is method of grilling meat and vegetables on a grill built into the dining table.", "action": "eating Korean BBQ"},
        {"name": "Korean tofu soup", "description": "Korean tofu soup/stew or Sundubu jjigae is made from soft tofu, vegetables, thinly sliced meat/seafood, and chili paste. The dish is cooked directly in the small serving dish.", "action": "eating Korean tofu soup"},
        {"name": "hot pot", "description": "Hot pot originated in China and is a method of cooking protein and vegetables in boiling broth similar to fondue.", "action": "eating hot pot"},
        {"name": "naan", "description": "Naan is an oven-baked flatbread often eaten with South Asian foods with curries.", "action": "eating naan"},
        {"name": "paneer dish", "description": "Paneer is a non-aged, non-melting soft cheese common in Indian food.", "action": "eating a paneer dish"},
        {"name": "lassi drink", "description": "Lassi is a traditional yogurt-based drink from the Indian subcontinent and can often be flavored and sweetened with mango.", "action": "drinking a lassi"},
        {"name": "Thai iced tea", "description": "Thai iced tea is made from strongly brewed black tea and sweetened with sugar and condensed milk, served cold.", "action": "drinking Thai iced tea"},
        {"name": "mochi", "description": "Mochi is a Japanese rice cake made from glutinous rice and is sometimes flavored or with a sweet filling.", "action": "eating mochi"},
        {"name": "halo halo", "description": "Halo halo is a Filipino cold dessert made up of crushed ice, evaporated/condensed milk, ice cream, and with toppings that can include: ube, sweetened beans, cocunut strips, taro.", "action": "eating halo halo"},
        {"name": "adobo", "description": "Adobo is a Filipino dish that involves a protein or vegetables marinated in vinegar, soy sauce, garlic, bay leaves, and pepper.", "action": "eating adobo"},
        {"name": "teriyaki", "description": "Teriyaki is a cooking technique used in Japanese cuisine where foods are boiled/grilled with a glaze of soy sauce, rice wine, and sugar.", "action": "eating teriyaki"},
        {"name": "Thai curry", "description": "Thai curries often include vegetables or a protein cooked in a sauce based on a paste made from chilies, onions, garlic. Curries from some parts of Thailand include coconut milk.", "action": "eating Thai curry"},
        {"name": "spam musubi", "description": "Spam musubi is a snack composed of grilled spam on a block of rice, wrapped with nori.", "action": "eating spam musubi"},
        {"name": "peking duck", "description": "Peking duck is a dish from Beijing that involves eating crispy duck skin in a thin pancake/bun with scallions and sweet bean sauce.", "action": "peking duck"},
        {"name": "kalua pig", "description": "Kalua pig is a traditional Hawaiian style pork slow-roasted/smoked.", "action": "eating kalua pig"},
        {"name": "poke", "description": "Poke is diced raw fish marinated in various sauces and served as an appetizer or over a bowl or rice or vegetables with toppings.", "action": "eating poke"},
        {"name": "teppanyaki", "description": "Teppanyaki is a style of Japanese cuisine where protein and vegetables are cooked on a large iron griddle.", "action": "eating teppanyaki"},
        {"name": "samosa", "description": "A samosa is a South Asian fried pastry filled with spiced potatoes, onions, peas, lentils, and meat.", "action": "eating a samosa"},
        {"name": "satay", "description": "Satay is an Indonesian dish of seasoned, skewered meat grilled with a sauce, often a peanut sauce.", "action": "eating a satay"},
        {"name": "bibambap", "description": "Bibambap is a Korean rice dish topped with vegetables, kimchi, and often with an egg and sliced meat.", "action": "eating bibambap"},
        {"name": "Vietnamese iced coffee", "description": "Vietnamese iced coffee is typically hot coffee poured into a glass full of ice and served with sweetened condensed milk.", "action": "drinking Vietnamese iced coffee"},
        {"name": "dim sum", "description": "Dim sum is a Chinese type of cuisine where there are many small dishes that are often steamed or fried and served in small bamboo steamers.", "action": "eating dim sum"},
    ]
    return eat
    
if __name__ == '__main__':
    main()