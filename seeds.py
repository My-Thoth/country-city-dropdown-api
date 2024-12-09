from app import create_app, db  # Import app and db
from app.models import Country, City  # Import the Country and City models directly from models

def seed_countries():
    """Seed the Country table with hardcoded country data and create cities for each country."""
    app = create_app()  # Get both app and db
    
    with app.app_context():
        # Step 1: Avoid deleting any data from the Country and City tables
        print("Skipping deletion of existing data in the database.")
        
        # Hardcoded list of countries (code, name, region)
        countries_data = countries_data = [
    {"code": "AF", "name": "Afghanistan", "region": "Asia"},
    {"code": "AL", "name": "Albania", "region": "Europe"},
    {"code": "DZ", "name": "Algeria", "region": "Africa"},
    {"code": "AD", "name": "Andorra", "region": "Europe"},
    {"code": "AO", "name": "Angola", "region": "Africa"},
    {"code": "AR", "name": "Argentina", "region": "South America"},
    {"code": "AM", "name": "Armenia", "region": "Asia"},
    {"code": "AU", "name": "Australia", "region": "Oceania"},
    {"code": "AT", "name": "Austria", "region": "Europe"},
    {"code": "AZ", "name": "Azerbaijan", "region": "Asia"},
    {"code": "BS", "name": "Bahamas", "region": "North America"},
    {"code": "BH", "name": "Bahrain", "region": "Asia"},
    {"code": "BD", "name": "Bangladesh", "region": "Asia"},
    {"code": "BB", "name": "Barbados", "region": "North America"},
    {"code": "BY", "name": "Belarus", "region": "Europe"},
    {"code": "BE", "name": "Belgium", "region": "Europe"},
    {"code": "BZ", "name": "Belize", "region": "North America"},
    {"code": "BJ", "name": "Benin", "region": "Africa"},
    {"code": "BT", "name": "Bhutan", "region": "Asia"},
    {"code": "BO", "name": "Bolivia", "region": "South America"},
    {"code": "BA", "name": "Bosnia and Herzegovina", "region": "Europe"},
    {"code": "BW", "name": "Botswana", "region": "Africa"},
    {"code": "BR", "name": "Brazil", "region": "South America"},
    {"code": "BN", "name": "Brunei Darussalam", "region": "Asia"},
    {"code": "BG", "name": "Bulgaria", "region": "Europe"},
    {"code": "BF", "name": "Burkina Faso", "region": "Africa"},
    {"code": "BI", "name": "Burundi", "region": "Africa"},
    {"code": "KH", "name": "Cambodia", "region": "Asia"},
    {"code": "CM", "name": "Cameroon", "region": "Africa"},
    {"code": "CA", "name": "Canada", "region": "North America"},
    {"code": "CV", "name": "Cabo Verde", "region": "Africa"},
    {"code": "CF", "name": "Central African Republic", "region": "Africa"},
    {"code": "TD", "name": "Chad", "region": "Africa"},
    {"code": "CL", "name": "Chile", "region": "South America"},
    {"code": "CN", "name": "China", "region": "Asia"},
    {"code": "CO", "name": "Colombia", "region": "South America"},
    {"code": "KM", "name": "Comoros", "region": "Africa"},
    {"code": "CG", "name": "Congo", "region": "Africa"},
    {"code": "CD", "name": "Democratic Republic of the Congo", "region": "Africa"},
    {"code": "CR", "name": "Costa Rica", "region": "North America"},
    {"code": "HR", "name": "Croatia", "region": "Europe"},
    {"code": "CU", "name": "Cuba", "region": "North America"},
    {"code": "CY", "name": "Cyprus", "region": "Europe"},
    {"code": "CZ", "name": "Czech Republic", "region": "Europe"},
    {"code": "CI", "name": "Côte d'Ivoire", "region": "Africa"},
    {"code": "DK", "name": "Denmark", "region": "Europe"},
    {"code": "DJ", "name": "Djibouti", "region": "Africa"},
    {"code": "DM", "name": "Dominica", "region": "Caribbean"},
    {"code": "DO", "name": "Dominican Republic", "region": "North America"},
    {"code": "EC", "name": "Ecuador", "region": "South America"},
    {"code": "EG", "name": "Egypt", "region": "Africa"},
    {"code": "SV", "name": "El Salvador", "region": "North America"},
    {"code": "GQ", "name": "Equatorial Guinea", "region": "Africa"},
    {"code": "ER", "name": "Eritrea", "region": "Africa"},
    {"code": "EE", "name": "Estonia", "region": "Europe"},
    {"code": "ET", "name": "Ethiopia", "region": "Africa"},
    {"code": "FJ", "name": "Fiji", "region": "Oceania"},
    {"code": "FI", "name": "Finland", "region": "Europe"},
    {"code": "FR", "name": "France", "region": "Europe"},
    {"code": "GA", "name": "Gabon", "region": "Africa"},
    {"code": "GM", "name": "Gambia", "region": "Africa"},
    {"code": "GE", "name": "Georgia", "region": "Asia"},
    {"code": "DE", "name": "Germany", "region": "Europe"},
    {"code": "GH", "name": "Ghana", "region": "Africa"},
    {"code": "GR", "name": "Greece", "region": "Europe"},
    {"code": "GD", "name": "Grenada", "region": "Caribbean"},
    {"code": "GT", "name": "Guatemala", "region": "North America"},
    {"code": "GN", "name": "Guinea", "region": "Africa"},
    {"code": "GW", "name": "Guinea-Bissau", "region": "Africa"},
    {"code": "GY", "name": "Guyana", "region": "South America"},
    {"code": "HT", "name": "Haiti", "region": "Caribbean"},
    {"code": "HN", "name": "Honduras", "region": "North America"},
    {"code": "HU", "name": "Hungary", "region": "Europe"},
    {"code": "IS", "name": "Iceland", "region": "Europe"},
    {"code": "IN", "name": "India", "region": "Asia"},
    {"code": "ID", "name": "Indonesia", "region": "Asia"},
    {"code": "IR", "name": "Iran", "region": "Asia"},
    {"code": "IQ", "name": "Iraq", "region": "Asia"},
    {"code": "IE", "name": "Ireland", "region": "Europe"},
    {"code": "IL", "name": "Israel", "region": "Asia"},
    {"code": "IT", "name": "Italy", "region": "Europe"},
    {"code": "JM", "name": "Jamaica", "region": "Caribbean"},
    {"code": "JP", "name": "Japan", "region": "Asia"},
    {"code": "JO", "name": "Jordan", "region": "Asia"},
    {"code": "KZ", "name": "Kazakhstan", "region": "Asia"},
    {"code": "KE", "name": "Kenya", "region": "Africa"},
    {"code": "KI", "name": "Kiribati", "region": "Oceania"},
    {"code": "KR", "name": "Korea (Republic of)", "region": "Asia"},
    {"code": "KW", "name": "Kuwait", "region": "Asia"},
    {"code": "KG", "name": "Kyrgyzstan", "region": "Asia"},
    {"code": "LA", "name": "Lao People's Democratic Republic", "region": "Asia"},
    {"code": "LV", "name": "Latvia", "region": "Europe"},
    {"code": "LB", "name": "Lebanon", "region": "Asia"},
    {"code": "LS", "name": "Lesotho", "region": "Africa"},
    {"code": "LR", "name": "Liberia", "region": "Africa"},
    {"code": "LY", "name": "Libya", "region": "Africa"},
    {"code": "LI", "name": "Liechtenstein", "region": "Europe"},
    {"code": "LT", "name": "Lithuania", "region": "Europe"},
    {"code": "LU", "name": "Luxembourg", "region": "Europe"},
    {"code": "MO", "name": "Macao", "region": "Asia"},
    {"code": "MK", "name": "North Macedonia", "region": "Europe"},
    {"code": "MG", "name": "Madagascar", "region": "Africa"},
    {"code": "MW", "name": "Malawi", "region": "Africa"},
    {"code": "MY", "name": "Malaysia", "region": "Asia"},
    {"code": "MV", "name": "Maldives", "region": "Asia"},
    {"code": "ML", "name": "Mali", "region": "Africa"},
    {"code": "MT", "name": "Malta", "region": "Europe"},
    {"code": "MH", "name": "Marshall Islands", "region": "Oceania"},
    {"code": "MQ", "name": "Martinique", "region": "Caribbean"},
    {"code": "MR", "name": "Mauritania", "region": "Africa"},
    {"code": "MU", "name": "Mauritius", "region": "Africa"},
    {"code": "MX", "name": "Mexico", "region": "North America"},
    {"code": "FM", "name": "Micronesia (Federated States of)", "region": "Oceania"},
    {"code": "MD", "name": "Moldova", "region": "Europe"},
    {"code": "MC", "name": "Monaco", "region": "Europe"},
    {"code": "MN", "name": "Mongolia", "region": "Asia"},
    {"code": "ME", "name": "Montenegro", "region": "Europe"},
    {"code": "MA", "name": "Morocco", "region": "Africa"},
    {"code": "MZ", "name": "Mozambique", "region": "Africa"},
    {"code": "MM", "name": "Myanmar", "region": "Asia"},
    {"code": "NA", "name": "Namibia", "region": "Africa"},
    {"code": "NR", "name": "Nauru", "region": "Oceania"},
    {"code": "NP", "name": "Nepal", "region": "Asia"},
    {"code": "NL", "name": "Netherlands", "region": "Europe"},
    {"code": "NZ", "name": "New Zealand", "region": "Oceania"},
    {"code": "NI", "name": "Nicaragua", "region": "North America"},
    {"code": "NE", "name": "Niger", "region": "Africa"},
    {"code": "NG", "name": "Nigeria", "region": "Africa"},
    {"code": "NO", "name": "Norway", "region": "Europe"},
    {"code": "OM", "name": "Oman", "region": "Asia"},
    {"code": "PK", "name": "Pakistan", "region": "Asia"},
    {"code": "PW", "name": "Palau", "region": "Oceania"},
    {"code": "PA", "name": "Panama", "region": "North America"},
    {"code": "PG", "name": "Papua New Guinea", "region": "Oceania"},
    {"code": "PY", "name": "Paraguay", "region": "South America"},
    {"code": "PE", "name": "Peru", "region": "South America"},
    {"code": "PH", "name": "Philippines", "region": "Asia"},
    {"code": "PL", "name": "Poland", "region": "Europe"},
    {"code": "PT", "name": "Portugal", "region": "Europe"},
    {"code": "QA", "name": "Qatar", "region": "Asia"},
    {"code": "RO", "name": "Romania", "region": "Europe"},
    {"code": "RU", "name": "Russian Federation", "region": "Europe"},
    {"code": "RW", "name": "Rwanda", "region": "Africa"},
    {"code": "KN", "name": "Saint Kitts and Nevis", "region": "Caribbean"},
    {"code": "LC", "name": "Saint Lucia", "region": "Caribbean"},
    {"code": "VC", "name": "Saint Vincent and the Grenadines", "region": "Caribbean"},
    {"code": "WS", "name": "Samoa", "region": "Oceania"},
    {"code": "SM", "name": "San Marino", "region": "Europe"},
    {"code": "ST", "name": "Sao Tome and Principe", "region": "Africa"},
    {"code": "SA", "name": "Saudi Arabia", "region": "Asia"},
    {"code": "SN", "name": "Senegal", "region": "Africa"},
    {"code": "RS", "name": "Serbia", "region": "Europe"},
    {"code": "SC", "name": "Seychelles", "region": "Africa"},
    {"code": "SL", "name": "Sierra Leone", "region": "Africa"},
    {"code": "SG", "name": "Singapore", "region": "Asia"},
    {"code": "SK", "name": "Slovakia", "region": "Europe"},
    {"code": "SI", "name": "Slovenia", "region": "Europe"},
    {"code": "SB", "name": "Solomon Islands", "region": "Oceania"},
    {"code": "SO", "name": "Somalia", "region": "Africa"},
    {"code": "ZA", "name": "South Africa", "region": "Africa"},
    {"code": "SS", "name": "South Sudan", "region": "Africa"},
    {"code": "ES", "name": "Spain", "region": "Europe"},
    {"code": "LK", "name": "Sri Lanka", "region": "Asia"},
    {"code": "SD", "name": "Sudan", "region": "Africa"},
    {"code": "SR", "name": "Suriname", "region": "South America"},
    {"code": "SE", "name": "Sweden", "region": "Europe"},
    {"code": "CH", "name": "Switzerland", "region": "Europe"},
    {"code": "SY", "name": "Syrian Arab Republic", "region": "Asia"},
    {"code": "TW", "name": "Taiwan", "region": "Asia"},
    {"code": "TJ", "name": "Tajikistan", "region": "Asia"},
    {"code": "TZ", "name": "Tanzania (United Republic of)", "region": "Africa"},
    {"code": "TH", "name": "Thailand", "region": "Asia"},
    {"code": "TL", "name": "Timor-Leste", "region": "Asia"},
    {"code": "TG", "name": "Togo", "region": "Africa"},
    {"code": "TO", "name": "Tonga", "region": "Oceania"},
    {"code": "TT", "name": "Trinidad and Tobago", "region": "Caribbean"},
    {"code": "TN", "name": "Tunisia", "region": "Africa"},
    {"code": "TR", "name": "Turkey", "region": "Asia"},
    {"code": "TM", "name": "Turkmenistan", "region": "Asia"},
    {"code": "TC", "name": "Turks and Caicos Islands", "region": "Caribbean"},
    {"code": "TV", "name": "Tuvalu", "region": "Oceania"},
    {"code": "UG", "name": "Uganda", "region": "Africa"},
    {"code": "UA", "name": "Ukraine", "region": "Europe"},
    {"code": "AE", "name": "United Arab Emirates", "region": "Asia"},
    {"code": "GB", "name": "United Kingdom of Great Britain and Northern Ireland", "region": "Europe"},
    {"code": "US", "name": "United States of America", "region": "North America"},
    {"code": "UY", "name": "Uruguay", "region": "South America"},
    {"code": "UZ", "name": "Uzbekistan", "region": "Asia"},
    {"code": "VU", "name": "Vanuatu", "region": "Oceania"},
    {"code": "VE", "name": "Venezuela", "region": "South America"},
    {"code": "VN", "name": "Viet Nam", "region": "Asia"},
    {"code": "YE", "name": "Yemen", "region": "Asia"},
    {"code": "ZM", "name": "Zambia", "region": "Africa"},
    {"code": "ZW", "name": "Zimbabwe", "region": "Africa"},
]

        
        # Step 2: Seed countries into the Country table if they don't already exist
        for country in countries_data:
            code = country['code']
            name = country['name']
            region = country['region']

            # Check if the country already exists to avoid duplicates
            existing_country = Country.query.filter_by(code=code).first()
            if not existing_country:
                new_country = Country(code=code, name=name, region=region)
                db.session.add(new_country)
        
        db.session.commit()
        print("Countries seeded into the database.")

        # Step 3: Add cities for each country if they don't already exist
        cities_data = {
            "US": [
                "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
                "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
            ],
            "NG": [
                "Lagos", "Abuja", "Kano", "Ibadan", "Port Harcourt", 
                "Benin City", "Maiduguri", "Zaria", "Aba", "Kaduna"
            ]
        }

        # Step 4: Seed cities for each country
        for country in countries_data:
            country_code = country['code']
            country_name = country['name']

            # Retrieve the country object from the database
            country_obj = Country.query.filter_by(code=country_code).first()

            if country_obj:
                # Add cities for the country only if they don't already exist
                for city_name in cities_data.get(country_code, []):
                    existing_city = City.query.filter_by(name=city_name, country_id=country_obj.id).first()
                    if not existing_city:
                        new_city = City(name=city_name, country_id=country_obj.id)
                        db.session.add(new_city)
                
        db.session.commit()
        print("Cities seeded into the database.")

if __name__ == '__main__':
    seed_countries()
