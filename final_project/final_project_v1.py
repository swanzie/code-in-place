def main():
    eat = create_eat()
    watch = create_watch()
    listen = create_listen()
    read = create_read()
    another_response = True

    while another_response:
        date = what_date()
        category = what_category()
        response = get(date, category, eat, watch, listen, read) 
        print_response(date, response)
        another_response = another()

def another():
    another = input('Would you like another suggestion (y/n)? ')
    print("")
    if another == 'y':
        return True
    else:
        return False

def what_date():
    """
    ask user what day of month it is
    return that number as int
    """
    print("Happy Asian American and Pacific Islander Heritage Month!")
    print("We have a daily suggestion of how you can celebrate by eating, listening, reading, or watching.")
    date = int(input('What day of the month is it? '))
    return date

def what_category():
    """
    ask user what category they want to celebrate with
    return that category as string
    """
    category = input('Select how you want to celebrate: eat, listen, watch, read: ')
    is_valid = True
    while is_valid:
        if category == 'eat' or category == 'listen' or category == 'watch' or category == 'read':
            is_valid = False
        else:
            category = input('Not a valid cateogry. Select one of the following: eat, listen, watch, read: ')
    return category

def get(date, category, eat, watch, listen, read):
    i = date - 1
    response = {}
    if category == 'eat':
        response = eat[i]
    elif category == 'watch':
        response = watch[i]
    elif category == 'listen':
        response = listen[i]
    elif category == 'read':
        response = read[i]
    return response

def print_response(date, response):
    print("\nOn May " + str(date) + ", you can celebrate by " + response['action'] + ".")
    print(response['description'])
    print("Come back for another suggestion on how to celebrate AAPIHM tomorrow!\n")

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
        {"name": "hot pot", "description": "Hot pot originated in China and is a method of cooking protein and vegetables in boiling broth similar to fondue..", "action": "eating hot pot"},
        {"name": "naan", "description": "Naan is an oven-baked flatbread often eaten with South Asian foods with curries.", "action": "eating naan"},
        {"name": "paneer dish", "description": "Paneer is a non-aged, non-melting soft cheese common in Indian food.", "action": "eating a paneer dish"},
        {"name": "lassi drink", "description": "Lassi is a traditional yogurt-based drink from the Indian subcontinent and can often be flavored and sweetened with mango.", "action": "drinking a lassi"},
        {"name": "Thai iced tea", "description": "Thai iced tea is made from strongly brewed black tea and sweetened with sugar and condensed milk, served cold.", "action": "drinking Thai iced tea"},
        {"name": "mochi", "description": "Mochi is a Japanese rice cake made from glutinous rice and is sometimes flavored or with a sweet filling.", "action": "eating mochi"},
        {"name": "halo halo", "description": "Halo halo is a Filipino cold dessert made up of crushed ice, evaporated/condensed milk, ice cream, and with toppings that can include: ube, sweetened beans, cocunut strips, taro..", "action": "eating halo halo"},
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
    
def create_listen():
    """
    initialize list of dictionaries options to celebrate with listening
    """
    listen = [
        {"name":"Mike Shinoda", "description": "Mike Shinoda is an American musician, rapper, singer, songwriter and one of the co-founders of Linkin Park and Fort Minor", "action": "listening to Mike Shinoda on Spotify at https://open.spotify.com/artist/6xBZgSMsnKVmaAxzWEwMSD?si=5UrfmahLT9ucY1H3rYs3nQ"},
        {"name": "Far East Movement", "description": "Far East Movement is a hip hop/electronic group and the first Asian American group to earn a number one hit on the Billboard Hot 100 chart in October 2010", "action": "listening to Far East Movement on Spotify at https://open.spotify.com/artist/698hF4vcwHwPy8ltmXermq?si=SK6Qb_oNTmu2xa9hzSJ_RQ"},
        """
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        """
    ]
    return listen

def create_watch():
    """
    initialize list of dictionaries options to celebrate with watching
    """
    watch = [
        {"name":"Fresh Off the Boat", "description": "Fresh Off the Boat is a TV comedy series following Louis Huang and his family's relocation from Chinatown of Washington, DC to Orlando, Florida", "action": "watching Fresh Off the Boat on Hulu or Disney+"},
        {"name": "Kim's Convenience", "description": "Kim's Convenience is a Canadian TV sitcom centered on the Korean Canadian Kim family and their adventures in Toronto", "action": "watching Kim's Convenience on Netflix"},
        """
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        """
    ]
    return watch

def create_read():
    """
    initialize list of dictionaries options to celebrate with reading
    """

    read = [
        {"name":"Eat a Peach by David Chang & Gabe Ulla", "description": "This book explores David Chang's experience becoming a chef. Chang is the star of Netflix's Ugly Delicious.", "action": "reading Eat a Peach by David Chang & Gabe Ulla"},
        {"name": "Interior Chinatown by Charles Yu", "description": "Interior Chinatown is a personal novel about race, pop culture, immigration, assimilation.", "action": "reading Interior Chinatown by Charles Yu"},
        """
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        {"name": "", "description":"", "action": ""},
        """
    ]
    return read

if __name__ == '__main__':
    main()