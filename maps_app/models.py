from django.db import models
import urllib.request
import requests
import json
import string
import pprint
import re

class Hangouts_Model(models.Model):
    # at least 2 addreses need to be filled in
    add_1 = models.CharField(max_length=150, blank=False)
    add_2 = models.CharField(max_length=150, blank=False)
    add_3 = models.CharField(max_length=150, blank=True)
    add_4 = models.CharField(max_length=150, blank=True)
    add_5 = models.CharField(max_length=150, blank=True)
    add_6 = models.CharField(max_length=150, blank=True)
    add_7 = models.CharField(max_length=150, blank=True)
    add_8 = models.CharField(max_length=150, blank=True)
    add_9 = models.CharField(max_length=150, blank=True)
    add_10 = models.CharField(max_length=150, blank=True)
    centerpoint_radius = models.IntegerField(default=400)
    key = "AIzaSyBfoGge77ELb4mp-NDrl6R2H4AgP9tXrpo"
    
    categories = [
        ('cafe', 'Cafes'),
        ('bar', 'Bars'),
        ('gym', 'Gyms'),
        ('restaurant', 'Restaurants'), 
        ('shopping_mall', 'Shopping Malls'),
        ('subway_station', 'Subway Stations')
    ]

    # adding CharField with choice option, just add to the list of attributes in forms.py, don't forget to makemigrations again.
    category = models.CharField(max_length=100, choices=categories)
    
    # initialize attributes from methods
    def initialize(self):
        user_addrs_raw = [self.add_1, self.add_2, self.add_3, self.add_4, self.add_5, self.add_6, self.add_7, self.add_8, self.add_9, self.add_10]
        
        # only include addresses that are filled in 
        self.user_addrs = [add for add in user_addrs_raw if add != '']

        # calling and initializing other methods
        self.usr_addrs_crds = self.usr_input_to_crds(self.user_addrs)  
        self.cntpnt = self.find_cntpnt()

        # additional info for use in HTML
        self.no_users_list = [user + 1 for user in range(len(self.user_addrs))]
        self.user_addrs_no = list(zip(self.no_users_list, self.user_addrs))

        for cats in self.categories:
            if self.category == cats[0]:
                self.category_result = cats[1]
        
        self.autocomplete()
        

    # pull all values of specified key from nested JSON.
    def extract_values_json(self, obj, key):
        """ 
        type obj: Dict
        type key: str
        rtype results : List[str]
        """
        arr = []
        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        results = extract(obj, arr, key)
        return results

    # returns coordinates given string location input
    def usr_input_to_crds(self, user_addrs):
        """ 
        type user_addrs : List[str]
        rtype user_addrs_crds_mtd : List[tuple(float)]
        """
        # converting to text url friendly format
        user_addrs = list(map(lambda loc: loc.replace(" ", "%20"), user_addrs))
        
        # distinguish between user address coordinates for the method and class
        user_addrs_crds_mtd = []
        # places API basic url string
        places_API_basic_str = "https://maps.googleapis.com/maps/api/place/findplacefromtext/"
        output = "json?"

        # extract the coordinates for each user_addrs
        for addrs in user_addrs:    
            parameters = f"input={addrs}&inputtype=textquery&fields=geometry"
            request = f'{places_API_basic_str}{output}{parameters}&key={self.key}'
            response = urllib.request.urlopen(request).read()
            json_file = json.loads(response)
            user_addrs_crds_mtd.append((self.extract_values_json(json_file, 'lat')[0], self.extract_values_json(json_file, 'lng')[0]))
        
        return user_addrs_crds_mtd

    # calculate the centerpoint of all the coordinates
    def find_cntpnt(self):
        """ 
        rtype dis_dur : List[float]
        """
        crd_total = [sum(crd) for crd in zip(*self.usr_addrs_crds)]
        center_pnt = list(map(lambda crd: crd/len(self.usr_addrs_crds), crd_total))
        return center_pnt

    # The API for the embedded map only takes in formatted address as parameter; the coordinates are converted to place_id and then to formatted address. 
    def maps_embed_hangouts(self):
        """ 
        rtype str
        """
        # search for a nearby location
        places_search_API_basic_str = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={self.cntpnt[0]},{self.cntpnt[1]}&rankby=distance&key={self.key}'
        
        response = urllib.request.urlopen(places_search_API_basic_str).read()
        results_id = self.extract_values_json(json.loads(response), 'place_id')

        # convert id to formatted address
        places_details_API_basic_str = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={results_id[0]}&fields=formatted_address&key={self.key}'
        response = urllib.request.urlopen(places_details_API_basic_str).read()
        self.results_add = self.extract_values_json(json.loads(response), 'formatted_address')[0]

        # enter formatted address into Embedded Map API request.
        embedded_map_API_basic_str = f"https://www.google.com/maps/embed/v1/search?key={self.key}&"
        self.results_add = self.results_add.replace(" ","+")  
        request_map = f"{embedded_map_API_basic_str}q={self.category}+near+{self.results_add}" 
        print (request_map)
        return request_map

    # returns static map url with user address as markers.
    def maps_static_users(self):
        """ 
        rtype request : str
        """
        static_map_API_basic_str = "https://maps.googleapis.com/maps/api/staticmap?"
        markers_str = [f"&markers=color:purple%7Clabel:{i+1}%7C{self.usr_addrs_crds[i][0]},{self.usr_addrs_crds[i][1]}" for i in range(len(self.usr_addrs_crds))]
        markers_str = "".join(markers_str)
        request = f"{static_map_API_basic_str}size=640x640&scale=2&markers=color:red%7Clabel:C%7C{self.cntpnt[0]},{self.cntpnt[1]}{markers_str}&key={self.key}"
        return request

    def autocomplete(self):
        """ 
        rtype List[str]
        """
        autocom_API_basic_str = f'https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bandar+Tasik&key={self.key}'
        response = urllib.request.urlopen(autocom_API_basic_str).read()
        # pprint.pprint (json.loads(response))
        autocom_results = self.extract_values_json(json.loads(response), 'description')
        return autocom_results
        