from flask import Flask, jsonify

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return "Welcome to the IPL Match API!"

# Match detail route
@app.route('/match/<int:match_id>')
def match_detail(match_id):
    # Here you would normally retrieve match details from a database or API
    return jsonify({'match_id': match_id, 'details': 'Details of match id ' + str(match_id)})

# API endpoint for getting live matches
@app.route('/api/live-matches')
def live_matches():
    # Dummy data for live matches
    live_data = [{'match_id': 1, 'team1': 'Team A', 'team2': 'Team B', 'status': 'Live'},
                 {'match_id': 2, 'team1': 'Team C', 'team2': 'Team D', 'status': 'Live'}]
    return jsonify(live_data)

# API endpoint for ball-by-ball data
@app.route('/api/ball-by-ball/<int:match_id>')
def ball_by_ball(match_id):
    # Dummy data for ball-by-ball update
    ball_data = [{'over': 1, 'ball': 1, 'runs': 1, 'batsman': 'Batsman A'},
                 {'over': 1, 'ball': 2, 'runs': 4, 'batsman': 'Batsman B'}]
    return jsonify(ball_data)

if __name__ == '__main__':
    app.run(debug=True)
