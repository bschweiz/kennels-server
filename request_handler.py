import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals
from animals import get_single_animal
from animals import create_animal
from animals import delete_animal
from animals import update_animal
from locations import get_all_locations
from locations import get_single_location
from locations import create_location
from locations import delete_location
from locations import update_location
from customers import get_all_customers
from customers import get_single_customer
from customers import create_customer
from customers import delete_customer
from customers import update_customer
from employees import get_all_employees
from employees import get_single_employee
from employees import create_employee
from employees import delete_employee
from employees import update_employee

# Here's a class. It inherits from another class.
# For now, think of a class as a container for functions that
# work together for a common purpose. In this case, that
# common purpose is to respond to HTTP requests from a client.


class HandleRequests(BaseHTTPRequestHandler):

    # Here's a class function
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    # Another method! This supports requests with the OPTIONS verb.
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                        'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                        'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    #this is how we isolate the animal ID NUMBER FROM THE URL aka self.path 
    def parse_url(self, path):
        # Just like splitting a string in JavaScript. If the
        # path is "/animals/1", the resulting list will
        # have "" at index 0, "animals" at index 1, and "1"
        # at index 2.
        path_params = path.split("/")
        resource = path_params[1]
        id = None

        # Try to get the item at index 2
        try:
            # Convert the string "1" to the integer 1
            # This is the new parseInt()
            id = int(path_params[2])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id)  # This is a tuple

    # Here's a method on the class that overrides the parent's method.
    # It handles any GET request.
    def do_GET(self):
        # Set the response code to 'Ok'
        self._set_headers(200)
        response = {} #default response

        (resource, id) = self.parse_url(self.path)
        # It's if..else statements to check for various paths
        # First we check if it's animals
        if resource == "animals":
            if id is not None:
                response = f"{get_single_animal(id)}"
            else:
                response = f"{get_all_animals()}"
        #Then we check if it"s locations
        elif resource == "locations":
            if id is not None:
                response = f"{get_single_location(id)}"
            else:
                response = f"{get_all_locations()}"
        #Then we check if it"s employees
        elif resource == "employees":
            if id is not None:
                response = f"{get_single_employee(id)}"
            else:
                response = f"{get_all_employees()}"
        #And finally we check if it"s customers
        elif resource == "customers":
            if id is not None:
                response = f"{get_single_customer(id)}"
            else:
                response = f"{get_all_customers()}"

    # This weird code sends a response back to the client
        self.wfile.write(f"{response}".encode())

    # Here's a method on the class that overrides the parent's method.
    # It handles any POST request.
    def do_POST(self):
        # Set response code to 'Created'
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        #convert JSON STRING to PYTHON DICTIONARY!!!!!
        # .loads means LOAD-S "S" is for STRING
        post_body = json.loads(post_body)
        # PARSE THE URL, THIS CREATES A TUUUUUUUUUUUUUUUUUUUUUUUUUUIUUPLE!!
        (resource, id) = self.parse_url(self.path)
        # initialize new animal, location, whatever
        new_dictionary = None
        # check to see what the path aka resource was
        if resource == "animals":
            new_dictionary = create_animal(post_body)
        elif resource == "locations":
            new_dictionary = create_location(post_body)
        elif resource == "customers":
            new_dictionary = create_customer(post_body)
        elif resource == "employees":
            new_dictionary = create_employee(post_body)

        self.wfile.write(f"{new_dictionary}".encode())

    # adding delete functionality
    def do_DELETE(self):
        # Set a 204 response code
        self._set_headers(204)
        # Parse the URL
        (resource, id) = self.parse_url(self.path)
        # Delete a single animal from the list
        if resource == "animals":
            delete_animal(id)
        # Encode the new animal and send in response
        self.wfile.write("".encode())
        # Delete a single location from the list
        if resource == "locations":
            delete_location(id)
        # Encode the new location and send in response
            self.wfile.write("".encode())
        # Delete a single customer from the list
        if resource == "customers":
            delete_customer(id)
        # Encode the new customer and send in response
            self.wfile.write("".encode())
        # Delete a single customer from the list
        if resource == "employees":
            delete_employee(id)
        # Encode the new employee and send in response
            self.wfile.write("".encode())
        # Here"s a method on the class that overrides the parent's method.
        # It handles any PUT request.

    def do_PUT(self):
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        # parse the URL 
        (resource, id) = self.parse_url(self.path)
        # delete a single animal from the list
        if resource == "animals":
            update_animal(id, post_body)
            self.wfile.write("".encode())
        # delete a single location from the list
        if resource == "locations":
            update_location(id, post_body)
            self.wfile.write("".encode())
        # delete a single customer from the list
        if resource == "customers":
            update_customer(id, post_body)
            self.wfile.write("".encode())
        # delete a single employee from the list
        if resource == "employees":
            update_employee(id, post_body)
            self.wfile.write("".encode())

# This function is not inside the class. It is the starting
# point of this application.
def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
