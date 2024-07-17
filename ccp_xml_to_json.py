import xml.etree.ElementTree as ET
import json

def convert_unicode_escape_to_emoji(unicode_string):
    # Split the input string by the Unicode escape sequence
    parts = unicode_string.split("\\u")[1:]
    
    # Convert each part to an integer (base 16)
    code_points = [int(part, 16) for part in parts]
    
    # Join the characters to form the final emoji string
    emoji_string = ''.join(chr(cp) for cp in code_points)
    
    return emoji_string

# Function to convert country code to flag emoji in Unicode format
def country_code_to_unicode_emoji(country_code):
    return ''.join(f"\\u{ord(c):04X}" for c in country_code.upper().translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "🇦🇧🇨🇩🇪🇫🇬🇭🇮🇯🇰🇱🇲🇳🇴🇵🇶🇷🇸🇹🇺🇻🇼🇽🇾🇿")))

# Parse the XML file
tree = ET.parse('misc/ccp_english.xml')
root = tree.getroot()

# Extract countries and prepare the data
countries = []
for country in root.find('countries'):
    country_info = {
        'name': country.get('english_name'),
        'code': country.get('phone_code'),
        'flag': convert_unicode_escape_to_emoji(country_code_to_unicode_emoji(country.get('name_code')))
    }
    countries.append(country_info)


# Save the data to a JSON file
with open('misc/ccp_english.json', 'w', encoding='utf-16') as json_file:
    json.dump(countries, json_file, ensure_ascii=False, indent=4)

print("Countries data saved to misc/ccp_english.json")
