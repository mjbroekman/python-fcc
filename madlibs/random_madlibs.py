"""random_madlibs
Defines the available madlibs for madlib.py

madlibs: dict{
    Title: dict{
        "text" = string. User inputs are surrounded by ---
        "vars": dict{
            input_var: prompt_string,
            ...
        }
    },
    ...
}
"""
madlibs = {
    "Excerpt from Metro2033": {
        "text": "In the metro there were just a few places where the written word was ---past_tense_verb--- like this, and the inhabitants of ---abbreviation--- considered themselves to be one of the last strongholds of ---noun1---, the ---adjective1----most post of civilization on the ---train_line_name--- line. ---name1--- also read books and ---name2--- did too. ---name2--- awaited the return of ---possessive_pronoun_2--- friends from the ---place_generic1--- and when they arrived ---pronoun_of_2--- would ---verb--- up to them to ask if they'd brought anything ---condition_new_old---. And so, books almost always got into ---name2---'s ---body_part--- first, and then they went to the ---place_generic2---. ---name1---'s ---relative--- brought ---possessive_pronoun_1--- books from  ---possessive_pronoun_relative--- expeditions and they had almost a whole bookshelf of books in their ---noun_living_space---. The books lay on the ---noun2---, ---color1---ing and sometimes a little gnawed by mould and ---small_animal_plural---, sometimes sprinkled with ---color2--- specks of ---bodily_fluid---. They had things that no one else had, at the station and perhaps in the whole metro system: ---author_name1---, ---author_name2---, ---author_name3---, ---author_name4---, and some ---culture_name--- classics.",
        "vars": {
            "past_tense_verb": "Transitive Verb (past tense): ",
            "abbreviation": "Abbreviation: ",
            "noun1": "Noun: ",
            "adjective1": "Adjective (directional): ",
            "train_line_name": "Name of a train line: ",
            "name1": "Name: ",
            "name2": "Name (second): ",
            "possessive_pronoun_2": "Possessive Pronoun of second Name: ",
            "pronoun_of_2": "Regular Pronoun of Name: ",
            "place_generic1": "Place (generic): ",
            "verb": "Verb: ",
            "condition_new_old": "Adjective (condition): ",
            "body_part": "Part of the body: ",
            "place_generic2": "Place (generic): ",
            "relative": "Person (relation, not name): ",
            "possessive_pronoun_1": "Possessive Pronoun of first Name: ",
            "possessive_pronoun_relative": "Possessive Pronoun of relative: ",
            "noun_living_space": "Noun (living place): ",
            "noun2": "Noun (flat object): ",
            "color1": "Color: ",
            "small_animal_plural": "Small animal (plural): ",
            "color2": "Color: ",
            "bodily_fluid": "Bodily fluid: ",
            "author_name1": "Author's Last Name: ",
            "author_name2": "Author's Last Name (second): ",
            "author_name3": "Author's Last Name (third): ",
            "author_name4": "Author's Last Name (fourth): ",
            "culture_name": "Name of Culture: "
        },
    },
    "Lunar New Year": {
        "text": "Many people celebrate Lunar New Year in different ways all over the ---noun1---. \
            On this holiday, those in China who speak Cantonese, say 'Gung hay fat choy!' This means \
            . . . 'Wishing you ---plural_noun1--- and prosperity!' To them, and nearly ---number1--- \
            others, Lunar New Year is one of the most ---adjective1--- and important times of the year. \
            Also sometimes called Chinese New Year, this celebration is a time for everyone to get \
            together with their friends, favorite ---plural_noun2---, and even cousin ---person_in_room1---. \
            It is a time to honor their ancestors. Lunar New Year is a time to eat lots of \
            ---type_of_food_plural---. It is a time for ---adjective2--- beginnings, so go ahead and \
            buy a new ---adjective3--- ---article_of_clothing---. On New ---noun2---'s Eve, everyone \
            stays up late. Then, they go outside and light loud ---plural_noun3---. When the clock \
            strikes ---number2---, they open the doors and windows to their ---type_of_building---, \
            let the ---adjective4--- year out, and welcome the ---adjective5--- year in. Happy New Year!",
        "vars": {
            "noun1": "Noun: ",
            "plural_noun1": "Plural Noun: ",
            "number1": "Number: ",
            "adjective1": "Adjective: ",
            "plural_noun2": "Plural Noun: ",
            "person_in_room1": "Person in Room: ",
            "type_of_food_plural": "Type of Food (plural): ",
            "adjective2": "Adjective: ",
            "adjective3": "Adjective: ",
            "article_of_clothing": "Article of Clothing: ",
            "noun2": "Noun: ",
            "plural_noun3": "Plural Noun: ",
            "number2": "Number: ",
            "type_of_building": "Type of building: ",
            "adjective4": "Adjective: ",
            "adjective5": "Adjective: ",
        },
    },
}