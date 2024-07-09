import re
import json
import requests as rq
from bs4 import BeautifulSoup


class Ingredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


class Recipe:
    def __init__(self, name, id,  ingredients,  instructions,   rating, ratings_amount):
        self.name = name
        self.id = id
        self.ingredients = ingredients
        self.instructions = instructions
        self.rating = rating
        self.ratings_amount = ratings_amount

    """ @staticmethod
    def from_json(json_obj):
        name = json_obj['name']
        id = json_obj['id']
        category = Category(json_obj['category']['title'], id=json_obj['category']['id'])
        ingredients = [Ingredient(ingredient['name'], ingredient['amount']) for ingredient in json_obj['ingredients']]
        return Recipe(name, id, category, ingredients) """

    def __str__(self):
        return json.dumps({
            "name": self.name,
            "id": self.id,
            "ingredients": [ingredient.__dict__ for ingredient in self.ingredients],
            "instructions": self.instructions,
            "rating": self.rating,
            "ratings_amount": self.ratings_amount,
        }, ensure_ascii=False)


class ChefKochAPI:
    base_url = "https://www.chefkoch.de/"

    @staticmethod
    def parse_recipes(category, end_index=0, start_index=0):
        page_index = start_index
        recipe_index = 0
        recipe_amount = None
        requests_session = rq.Session()
        recipes = []
        # index = start_index
        while True:
            print("Parsing new recipes")
            # Actual part before .html is irrelevant, but site wont serve any results if missing
            response = requests_session.get(ChefKochAPI.base_url + 'rs/s'+str(page_index)+category)
            if response.status_code == 404:
                return
            soup = BeautifulSoup(response.text, 'lxml')
            if recipe_amount is None:
                recipe_amount_string = soup.find_all("span", {"class": "ds-text-category"})[0]
                recipe_amount = int(recipe_amount_string.get_text().strip().split(" ")[0].replace(".", ""))
                print("Crawling " + category)
            page_index += 1
            for recipe_list_item in soup.find_all("a", {"class": "ds-recipe-card__link ds-teaser-link"}):

                recipe_id = recipe_list_item['href'].replace("https://www.chefkoch.de/rezepte/", "")
                #print(recipe_list_item['href'])
                recipe_id = recipe_id[0: recipe_id.index('/')]
                recipe_url = recipe_list_item['href']
                recipe_response = requests_session.get(recipe_url)

                if recipe_response.status_code != 200:
                    continue
                
                recipe_soup = BeautifulSoup(recipe_response.text, 'lxml')
                

                if hasattr(recipe_soup.find("h1"), 'contents'):
                    recipe_name = recipe_soup.find("h1").contents[0]
                    print(recipe_name)
                    ingredients_tables = recipe_soup.find_all("table", {"class": "ingredients"})
                    recipe_ingredients = []
                    for ingredients_table in ingredients_tables:
                        ingredients_table_body = ingredients_table.find("tbody")
                        for row in ingredients_table_body.find_all('tr'):
                            cols = row.find_all('td')
                            recipe_ingredients.append(
                                Ingredient(re.sub(' +', ' ', cols[1].text.strip().replace(u"\u00A0", " ")),
                                        re.sub(' +', ' ', cols[0].text.strip().replace(u"\u00A0", " "))))
                            
                    
                    recipe_instructions = ""
                    recipe_instructions_parent = recipe_soup.find("article", {"class": "ds-box ds-grid-float ds-col-12 ds-col-m-8 ds-or-3"})
                    if recipe_instructions_parent is not None:
                        recipe_instructions_element = recipe_instructions_parent.find("div")
                        if recipe_instructions_element is not None:
                            recipe_instructions = recipe_instructions_element.getText().strip().replace(u"\u00A0", " ")
                    
                                                          
                    recipe_rating = 5.0
                    recipe_ratings_amount = 0
                    recipe_rating_parent = recipe_soup.find("a", {"class": "toggle-btn ds-btn ds-btn-tertiary accordion-btn recipe-rating-btn bi-recipe-rating--closed"})
                    if recipe_rating_parent is not None:
                        recipe_rating_direct_parent = recipe_rating_parent.find("div", {"class": "ds-rating-avg"})
                        if recipe_rating_direct_parent is not None:
                            recipe_rating = float(recipe_rating_direct_parent.find("span").find("strong").getText().strip())
                        recipe_ratings_amount_direct_parent = recipe_rating_parent.find("div", {"class": "ds-rating-count"})
                        if recipe_ratings_amount_direct_parent is not None:
                            recipe_ratings_amount = int(recipe_ratings_amount_direct_parent.find("span").find_all("span")[1].getText().strip().replace(".", ""))
                            
                                                        
                    print(str(recipe_index) + " - ", sep=' ', end='', flush=True)
                    recipe_index += 1
                    
                    
                    recipes.append(Recipe(recipe_name.replace(u"\u00A0", " "), recipe_id.replace(u"\u00A0", " "),
                                recipe_ingredients, recipe_instructions,
                                recipe_rating, recipe_ratings_amount))
                    
            if(page_index >= end_index):
                break
                    
        return recipes


class DataParser:

    @staticmethod
    def write_recipes_to_json(file_path, recipes, ):
        with open(file_path + ".json", "w") as txt_file:
            txt_file.write("[")
            for recipe in recipes:
                try:
                    txt_file.write(str(recipe))
                    txt_file.write(",")
                except Exception:
                    pass
            txt_file.write("{}]")

