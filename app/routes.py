from flask import Blueprint, jsonify
from flask import render_template, Flask
from app.models import Country, City

def initialize_routes(app, db):
    # Register API blueprint
    api = Blueprint('api', __name__, url_prefix='/api')

    # Test route to check if the blueprint is registered
    @api.route('/', methods=['GET'])
    def api_home():
        return jsonify({"message": "API is up and running!"})

    # Route to fetch all countries with trailing slash for consistency
    @api.route('/countries/', methods=['GET'])  # Added trailing slash here
    def get_countries():
        countries = Country.query.all()
        countries_list = [{'code': country.code, 'name': country.name, 'region': country.region} for country in countries]
        return jsonify(countries_list)

    # Route to fetch all cities with trailing slash for consistency
    @api.route('/cities/', methods=['GET'])
    def get_cities():
        cities = City.query.all()
        cities_list = [{'id': city.id, 'name': city.name, 'country_id': city.country_id} for city in cities]
        return jsonify(cities_list)

    # Route to fetch cities by country code
    @api.route('/countries/<string:country_code>/cities/', methods=['GET'])
    def get_cities_by_country(country_code):
        country = Country.query.filter_by(code=country_code).first()
        if not country:
            return jsonify({"message": "Country not found"}), 404
        
        cities = City.query.filter_by(country_id=country.id).all()
        cities_list = [{'id': city.id, 'name': city.name, 'country_id': city.country_id} for city in cities]
        return jsonify(cities_list)
    
    @app.route('/select-country', methods=['GET', 'POST'])
    def select_country():
    # Create a simple form dynamically
        countries = Country.query.all()  # Fetch countries from your database
        return render_template('select_country.html', countries=countries)
    
    @app.route('/update-cities/<country_code>', methods=['GET'])
    def update_cities(country_code):
    # Query for the country using the country_code
        country = Country.query.filter_by(code=country_code).first()
    
        if country:
            cities = City.query.filter_by(country_id=country.id).all()
            city_names = [city.name for city in cities]
            return jsonify({'cities': city_names})



    # Register the blueprint with the app
    app.register_blueprint(api)
