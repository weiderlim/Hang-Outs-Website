// load Google Maps JS autocomplete API. The initAutocomplete function is initialized automatically because of the callback in the HTTP request in the url sent.

function initAutocomplete() {
    // set autocomplete bounds to around the Singapore-Johor Area. Geolocate does not work here, perhaps hosting on apache solves this problem.
    var defaultBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(1.359989, 103.809223),
        new google.maps.LatLng(1.432752, 103.626575));
        
    var options = {
        bounds : defaultBounds,
    };

    // creating a list and store the Autocomplete objects in the list.
    const instanceList = [];
    for (let i = 0; i < 10; i++){
        instanceList[i] = new google.maps.places.Autocomplete(document.getElementById(`id_add_${i + 1}`), options);
    }

    // Avoid paying for data that you don't need by restricting the set of
    // place fields that are returned to just the address components. When the user selects an address from the drop-down, populate the address fields in the form.
    for (let obj of instanceList){
        obj.setFields(['address_component']); 
    }
}

// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(function(position) {
        var geolocation = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        var circle = new google.maps.Circle(
            {center: geolocation, radius: position.coords.accuracy});
        autocomplete.setBounds(circle.getBounds());
      });
    }
  }

