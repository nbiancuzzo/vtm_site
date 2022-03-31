from flask import Flask
from flask import render_template, request


app = Flask(__name__)

def findTotalCost(height, radius):
    pi = 3.14
    areaTop = pi * (radius**2)
    areaSide = 2*(pi*(radius*height))
    totalArea = areaTop + areaSide
    totalAreaSqFt = totalArea/144
    totalMaterialCost = 25 * totalAreaSqFt
    totalLaborCost = 15 * totalAreaSqFt
    totalCostEst = totalMaterialCost + totalLaborCost
    return totalCostEst


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

@app.route('/estimate', methods=['POST'])
def tankCalc():
    if request.method == 'POST':
        form = request.form
        height = float(form['height'])
        radius = float(form['radius'])

        tankCost = findTotalCost(height, radius)
        
        return render_template('estimate.html', tankEst = tankCost)
    return render_template('estimate')

if __name__ == '__main__':
    app.run(debug=True)