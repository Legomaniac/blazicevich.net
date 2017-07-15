Title: BrickLink

One of my favorite pastimes is buying and selling Lego, usually from Craiglist or eBay over to BrickLink, with my father Matt.

Here's a link to the store: <a href="http://www.bricklink.com/store/home.page?p=MattNJames">BozemanBricks</a>

I've also mapped out a city-level view in Google Maps of all the locations of orders to my store. I love seeing how global this hobby can be.

Check it out:

<html>
<head>

<script src = "http://maps.googleapis.com/maps/api/js?key=AIzaSyDE-9MrJeFHymAJkr4GIO8Za8y2B4HSE3E"></script>

<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-40427139-2', 'auto');
  ga('send', 'pageview');
</script>

</head>

<body>
<div id="map" style="height:450px"/>
</body>

<script>

var locations = [
['Mt. Pleasant, SC', 32.832322, -79.828426],
['Olympia, WA', 47.037874, -122.900695],
['Charlotte Hall, MD', 38.480956, -76.778022],
['Spirit Lake, IA', 43.422619, -95.102231],
['Miami, FL', 25.761680, -80.19179],
['Stone Mountain, GA', 33.808161, -84.170196],
['Spokane, WA', 47.658780, -117.426047],
['Bozeman, MT', 45.676998, -111.042934],
['Chandler, AZ', 33.306160, -111.84125],
['Rotterdam, Netherlands', 51.924420, 4.477733],
['Scottsdale, AZ', 33.494170, -111.926052],
['Jonesboro, ME', 44.662577, -67.572494],
['South Riding, VA', 38.920945, -77.503879],
['Hopewell Jct, NY', 41.583982, -73.808744],
['Brunswick West, Victoria', -37.763542, 144.943924],
['South Yarra, Victoria', -37.840098, 144.995442],
['St. Joseph, MI', 42.093858, -86.489546],
['Wesley Chapel, FL', 28.182893, -82.364175],
['Illnau, Switzerland', 47.408622, 8.722936],
['Melbourne, FL', 28.083627, -80.608109],
['East Middlebury, VT', 43.973394, -73.106227],
['Belleview, FL', 29.055258, -82.06231],
['Kenai, AK', 60.554444, -151.258333],
['Lafayette, CO', 39.993596, -105.089706],
['Sandy, UT', 40.564978, -111.838973],
['Portland, OR', 45.523062, -122.676482],
['Round Hill, VA', 39.132605, -77.768605],
['Richmond Hill, ON', 43.882840, -79.440281],
['Portland, OR', 45.523062, -122.676482],
['Woodbury, MN', 44.923855, -92.95938],
['Orlando, FL', 28.538335, -81.379236],
['Kennewick, WA', 46.211246, -119.137234],
['Saint-Peterburg, Russia', 59.887365, 30.448825],
['Vancouver, WA', 45.638728, -122.661486],
['Tooele, UT', 40.530778, -112.29828],
['Bronx, NY', 40.837049, -73.86543],
['Mays Landing, NJ', 39.452339, -74.727663],
['Northville, MI', 42.431146, -83.483269],
['Greenfields, WA', -32.530451, 115.752303],
['Norwich, CT', 41.524265, -72.07591],
['Singapore, Singapore', 1.352083, 103.819836],
['Wichita, KS', 37.687176, -97.330053],
['Brooklyn, NY', 40.678178, -73.944158],
['Decatur, IL', 39.840315, -88.9548],
['Bozeman, MT', 45.676998, -111.042934],
['San Carlos, CA', 37.507159, -122.260522],
['Cambridge, MA', 42.373616, -71.109734],
['Great Falls, MT', 47.494184, -111.283345],
['Kaysville, UT', 41.035222, -111.938552],
['Jackson, MI', 42.245869, -84.401346],
['Albuquerque, NM', 35.085334, -106.605553],
['Millersburg, PA', 40.539529, -76.96081],
['San Francisco, CA', 37.774929, -122.419416],
['Princeton, NC', 35.465994, -78.16055],
['Houston, TX', 29.760427, -95.369803],
['Phoenix, AZ', 33.448377, -112.074037],
['Kirkland, WA', 47.681488, -122.208735],
['Conroe, TX', 30.311877, -95.456051],
['Gardena, CA', 33.888349, -118.308962],
['Portland, OR', 45.523062, -122.676482],
['Sylvan Lake, AL', 52.307620, -114.097995],
['Painesville, OH', 41.724488, -81.245657],
['Grand Rapids, MI', 42.963360, -85.668086],
['Fargo, ND', 46.877186, -96.789803],
['Mount Vernon, IN', 37.932266, -87.895027],
['Lethbridge, AL', 49.693490, -112.84184],
['Indianapolas, IN', 39.768403, -86.158068],
['Walnut Shade, MO', 36.732560, -93.193514]
];

var map = new google.maps.Map(document.getElementById('map'), {
  zoom: 2,
  center: new google.maps.LatLng(25, 0),
  mapTypeId: google.maps.MapTypeId.ROADMAP
});

var infowindow = new google.maps.InfoWindow();

var marker, i;

for (i = 0; i < locations.length; i++) {
  marker = new google.maps.Marker({
    position: new google.maps.LatLng(locations[i][1], locations[i][2]),
    icon: '/static/lego_brick.png',
    map: map
  });

  google.maps.event.addListener(marker, 'click', (function(marker, i) {
    return function() {
      infowindow.setContent(locations[i][0]);
      infowindow.open(map, marker);
    }
  })(marker, i));
}

google.maps.event.addDomListener(window, 'load', initialize);
google.maps.event.addDomListener(window, "resize", function() {
 var center = map.getCenter();
 google.maps.event.trigger(map, "resize");
 map.setCenter(center); 
});

</script>
</html>

