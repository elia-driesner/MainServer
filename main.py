from flask import Flask
from get_chefkoch import Search

app = Flask(__name__)

@app.route('/')
def index():
    return 'server running>'

@app.route('/recepieOfTheDay', methods=['GET'])
def recepieOfTheDay():
    try:
        recipe = Search().recipeOfTheDay()
    
        data = {
            'name': recipe.name,
            'image': str(recipe.image),
            'cookTime': str(recipe.cookTime),
            'prepTime': str(recipe.prepTime),
            'category': recipe.category,
            'ingredients': recipe.ingredients,
        }
        
        return data
    except Exception as e:
        print('Failed to recepieOfTheDay: ' + e)

if __name__ == '__main__':
    app.run(port=5002)

