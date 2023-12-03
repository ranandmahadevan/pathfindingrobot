from flask import Flask
import matrix_generation
import a_star
#import photo_gen

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/start")
def start_plan():
#    photo_gen.photo()
    matrix = matrix_generation.matrix_gen()
    path = a_star.a_star_algo(matrix,(0,0),(5,5))
    path.insert(0,(-1,len(path)))
    print(matrix)
    print(path)
    return path

