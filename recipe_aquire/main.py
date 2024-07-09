from chefkoch import ChefKochAPI, DataParser

LINKS = ["t30/Auflauf-Rezepte.html",
    "t51/Aufstrich-Rezepte.html",
    "t46/Brotspeise-Rezepte.html",
    "t98/Eier-Rezepte.html",
    "t81/Eintopf-Rezepte.html",
    "t100/Mehlspeisen-Rezepte.html",
    "t31/Pasta-Rezepte.html",
    "t82/Pizza-Rezepte.html",
    "t15/Salat-Rezepte.html",
    "t34/Saucen-Rezepte.html",
    "t40/Suppe-Rezepte.html",
    "t89/Suessspeise-Rezepte.html",
    "t32/Vegetarisch-Rezepte.html",
    "t24/Nudeln-Rezepte.html",
    "t37/Reis-Rezepte.html",
    "t138/Kartoffeln-Rezepte.html",
    "t61/Fisch-Rezepte.html",
    "t26/Krustentier-oder-Muscheln-Rezepte.html",
    "t16/Fleisch-Rezepte.html",
    "t109/Frucht-Rezepte.html",
    "t18/Gemuese-Rezepte.html",
    "t165/Huelsenfruechte-Rezepte.html",
    "t83/Kaese-Rezepte.html",
    "t36/Beilage-Rezepte.html",
    "t90/Dessert-Rezepte.html",
    "t53/Fruehstueck-Rezepte.html",
    "t21/Hauptspeise-Rezepte.html",
    "t19/Vorspeise-Rezepte.html",
    "t71/Snack-Rezepte.html",
    "t23/Backen-Rezepte.html",
    "t23,108/Backen-Brot-oder-Broetchen-Rezepte.html",
    "t23,104/Backen-Creme-Rezepte.html",
    "t127/Eis-Rezepte.html",
    "t23,147/Backen-Kekse-Rezepte.html",
    "t157/Konfiserie-Rezepte.html",
    "t23,92/Backen-Kuchen-Rezepte.html",
    "t23,122/Backen-Tarte-Rezepte.html",
    "t23,93/Backen-Torte-Rezepte.html",
    "t11/Getraenk-Rezepte.html",
    "t11,121/Getraenk-Bowle-Rezepte.html",
    "t10,11/Cocktail-Getraenk-Rezepte.html",
    "t10,11,126/Getraenk-alkoholfrei-Cocktail-Rezepte.html",
    "t11,156/Getraenk-Kaffee-Tee-oder-Kakao-Rezepte.html",
    "t11,151/Getraenk-Likoer-Rezepte.html",
    "t11,142/Getraenk-Punsch-Rezepte.html",
    "t11,113/Getraenk-Shake-Rezepte.html",
    "t78/Fruehling-Rezepte.html",
    "t120/Ostern-Rezepte.html",
    "t87/Silvester-Rezepte.html",
    "t27/Sommer-Rezepte.html",
    "t99/Herbst-Rezepte.html",
    "t39/Halloween-Rezepte.html",
    "t102/Weihnachten-Rezepte.html",
    "t64/Winter-Rezepte.html",
    "t101/Afrika-Rezepte.html",
    "t38/USA-oder-Kanada-Rezepte.html",
    "t14/Asien-Rezepte.html",
    "t14,76/Asien-China-Rezepte.html",
    "t13,14/Indien-Asien-Rezepte.html",
    "t14,148/Asien-Japan-Rezepte.html",
    "t14,123/Asien-Thailand-Rezepte.html",
    "t145/Australien-Rezepte.html",
    "t29/Europa-Rezepte.html",
    "t29,65/Europa-Deutschland-Rezepte.html",
    "t29,84/Europa-Frankreich-Rezepte.html",
    "t29,44/Europa-Griechenland-Rezepte.html",
    "t29,117/Europa-Grossbritannien-Rezepte.html",
    "t28,29/Italien-Europa-Rezepte.html",
    "t29,72/Europa-Oesterreich-Rezepte.html",
    "t29,149/Europa-Portugal-Rezepte.html",
    "t29,43/Europa-Spanien-Rezepte.html",
    "t103/Tuerkei-Rezepte.html",
    "t95/Karibik-und-Exotik-Rezepte.html",
    "t163/Mittlerer-und-Naher-Osten-Rezepte.html",
    "t86/Osteuropa-Rezepte.html",
    "t79/Basisrezepte-Rezepte.html",
    "t111/Babynahrung-Rezepte.html",
    "t152/Camping-Rezepte.html",
    "t150/Haltbarmachen-Rezepte.html",
    "t106/Festlich-Rezepte.html",
    "t146/Geheimrezept-Rezepte.html",
    "t63/Grillen-Rezepte.html",
    "t91/Kinder-Rezepte.html",
    "t45/Party-Rezepte.html",
    "t110/Resteverwertung-Rezepte.html"]


if __name__ == '__main__':
    index = 0
    file_size = 100
    for category in LINKS:
        
        recipes = []
        recipes_o3 = []
    
        for category_recipe in ChefKochAPI.parse_recipes(category, start_index=0, end_index=23):
            recipes.append(category_recipe)
        DataParser.write_recipes_to_json(str(category.replace(" ", "-").replace("/", "-")), recipes)

        #o3 Link
        bestRatedLink = category.split("/")
        bestRatedLink = bestRatedLink[0]+"o3/"+bestRatedLink[1]

        for category_recipe in ChefKochAPI.parse_recipes(bestRatedLink, start_index=0, end_index=23):
            recipes_o3.append(category_recipe)
        DataParser.write_recipes_to_json(str(bestRatedLink.replace(" ", "-").replace("/", "-")), recipes_o3)


        index += file_size
    
    
        