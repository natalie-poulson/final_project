console.log('what up')

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

  require(['leaflet-minimap'], function(MiniMap) {
    new Minimap(layer, options).addTo(map);
  });

// const mbxGeocoding = require('@mapbox/mapbox-sdk/services/geocoding');
// const geocodingClient = mbxGeocoding({ accessToken: 'pk.eyJ1IjoibmF0YWxpZXBsc24iLCJhIjoiY2psZm8ybnFnMHl4NDNwcG16eGFmMTdwaCJ9.2xYdBHCpcf5cdap8BvhVgQ' });

