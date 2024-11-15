import random
import string

# Function to generate a random string of a specific length
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate a unique index name by prepending "TestF16" to the random string
index_name = f"TestF16{generate_random_string()}"
index_name1 = f"TestF16{generate_random_string()}"
index_name2 = f"TestF16{generate_random_string()}"
index_name3 = f"TestF16{generate_random_string()}"


# Test data for creating an index
INDEX_DATA = {
    "addons": ["thumbnail"],
    "index_name": index_name,
    "engines": [
        {
            "engine_options": ["visual", "conversation", "text_in_video", "logo"],
            "engine_name": "marengo2.6"
        },
        {
            "engine_options": ["visual", "conversation"],
            "engine_name": "pegasus1.1"
        }
    ]
}

CREATE_FOR_DELETE = {
    "addons": ["thumbnail"],
    "index_name": index_name1,
    "engines": [
        {
            "engine_options": ["visual", "conversation", "text_in_video", "logo"],
            "engine_name": "marengo2.6"
        },
        {
            "engine_options": ["visual", "conversation"],
            "engine_name": "pegasus1.1"
        }
    ]
}

CREATE_TO_GET = {
    "addons": ["thumbnail"],
    "index_name": index_name2,
    "engines": [
        {
            "engine_options": ["visual", "conversation"],
            "engine_name": "pegasus1.1"
        }
    ]
}

# Invalid test data (for negative tests)
INVALID_INDEX_DATA = {
    "index_name": "",  # Missing index name
    "engines": [],
    "addons": []
}

MISSING_REQUIRED_FIELD = {
    "engines": [
        {
            "engine_name": "marengo2.6",
            "engine_options": ["visual"]
        }
    ],
    "addons": []
}


# Minimal test data for index (only the minimum required fields)
MINIMAL_INDEX_DATA = {
    "index_name": index_name3,
    "engines": [
        {
            "engine_name": "marengo2.6",
            "engine_options": ["visual"]
        }
    ],
    "addons": []
}
