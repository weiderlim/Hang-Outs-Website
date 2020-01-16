# Hang-Outs-Website
A website developed with Django framework (with SQLite) and deployed with Apache. Find your the best places to meet up with your friends and family with Google API's! 

# Requirements
Python 3.0+
Django 3.0+
Personal Google API key - Enter your personal Google API key in maps_app/models.py under Hangouts_Model. You will need to have registered for the API's listed in 'How it Works' below.

Please refer to requirement.txt for more information. 

# Disclaimers:
By no means are the results from this website guranteed to be up to date and reflect current geographical conditions. They are subjected to Google Maps API's that can be found at the Google Maps Platform.
The API's used in this website are the Places Search API, Places Details API, Maps Embed API, Query AutoComplete API and the Map Static API.
None of your personal information will be used in any way without your permission.

# How It Works:
Enter the category of places that you and your friends would like to meet up at and your addresses.
The coordinates of all the addresses collected and the center point is calculated by triangulation.
The Google Places API searches for nearby places with the specified category from the center point.
The Google Details API converts the coordinates from the result of the API above to a formatted addresses
The Google Maps Embed API and Google Map Static API uses the formatted address and center point coordinates to give visualisation of the results and locations of the addresses relative to the results.

# Known Issues:
Occasionally, there are results that does not fit the category. This is due to the Google API's returning such results based on Google user inputs, which might not be accurate.

