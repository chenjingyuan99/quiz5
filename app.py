# Jingyuan Chen 9629

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Sample data
food_data = [
    {"amount": 10, "food": "Apples", "category": "F"},
    {"amount": 2, "food": "Bananas", "category": "F"},
    {"amount": 40, "food": "Cherries", "category": "F"},
    {"amount": 1, "food": "Daikon", "category": "V"},
    {"amount": 10, "food": "Fig", "category": "F"},
    {"amount": 30, "food": "Grapes", "category": "F"},
    {"amount": 5, "food": "Peach", "category": "F"},
    {"amount": 12, "food": "Celery", "category": "V"},
    {"amount": 1, "food": "Watermelon", "category": "F"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pie_chart')
def pie_chart():
    min_amount = request.args.get('min', 5, type=int)
    max_amount = request.args.get('max', 20, type=int)
    
    filtered_data = [item for item in food_data 
                    if min_amount <= item['amount'] <= max_amount]
    
    return render_template('pie_chart.html', 
                         data=json.dumps(filtered_data),
                         min_amount=min_amount,
                         max_amount=max_amount)

@app.route('/bar_chart')
def bar_chart():
    min_amount = request.args.get('min', 5, type=int)
    max_amount = request.args.get('max', 20, type=int)
    
    filtered_data = [item for item in food_data 
                    if min_amount <= item['amount'] <= max_amount]
    
    # Sort by amount (smallest to largest for top to bottom display)
    filtered_data.sort(key=lambda x: x['amount'])
    
    return render_template('bar_chart.html', 
                         data=json.dumps(filtered_data),
                         min_amount=min_amount,
                         max_amount=max_amount)

@app.route('/scatter_chart', methods=['GET', 'POST'])
def scatter_chart():
    sample_data = []
    
    if request.method == 'POST':
        # Process form data
        for i in range(1, 11):  # Up to 10 points
            x = request.form.get(f'x{i}', type=int)
            y = request.form.get(f'y{i}', type=int)
            c = request.form.get(f'c{i}', type=int)
            
            # Only add point if all values are provided and valid
            if x is not None and y is not None and c is not None:
                if 0 <= x <= 50 and 0 <= y <= 50 and c in [1, 2, 3]:
                    sample_data.append({"x": x, "y": y, "c": c})
    # else:
    #     # Default sample data for GET request
    #     sample_data = [
    #         {"x": 10, "y": 20, "c": 1},
    #         {"x": 25, "y": 35, "c": 2},
    #         {"x": 40, "y": 15, "c": 3},
    #         {"x": 15, "y": 45, "c": 1},
    #         {"x": 35, "y": 25, "c": 2}
    #     ]
    
    return render_template('scatter_chart.html', 
                         data=json.dumps(sample_data))


if __name__ == '__main__':
    app.run(debug=True)
