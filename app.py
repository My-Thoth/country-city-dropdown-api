from app import create_app  # Import the create_app function from __init__.py
from app.routes import initialize_routes  # Import initialize_routes
from flask_cors import CORS

# Initialize the app and db using the factory function
app, db = create_app()

# Initialize routes with the app and db
initialize_routes(app, db)

# Enable CORS for the entire app
CORS(app)


# Print all registered routes for debugging purposes
print(app.url_map)

if __name__ == "__main__":
    app.run(debug=True)
