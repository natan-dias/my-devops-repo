from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    """
    Simple root route to test if the service is running.
    ---
    responses:
      200:
        description: Hello World
    """
    return "Hello World"

@app.route('/get-user/<user_id>') #Dynamic value to be passed
def get_user(user_id):
    """
    Get a user by ID

    Parameters:
        user_id (str): The ID of the user

    Query Parameters:
        extra (str): Additional data to be included in the response

    Returns:
        A JSON object containing the user data
    """
    user_data = {
        'id': user_id,
        'name': 'John Doe',
        'email': 'Q5i9o@example.com'
    }

    extra = request.args.get('extra') #Query parameters
    if extra:
        user_data['extra'] = extra

    return jsonify(user_data), 200

# Create user

@app.route('/create-user', methods=['POST'])
def create_user():
    """
    Create a new user

    Body:

        {
            "name": str,
            "email": str
        }

    Returns:
        A JSON object containing the created user data
    """
    data = request.get_json()
    
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True)