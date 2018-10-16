console.log('what up')

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

  $('#mapModal').on('show.bs.modal', function(){
    setTimeout(function() {
      modalMap.invalidateSize();
    }, 10);
   });

const mbxGeocoding = require('@mapbox/mapbox-sdk/services/geocoding');
const geocodingClient = mbxGeocoding({ accessToken: 'pk.eyJ1IjoibmF0YWxpZXBsc24iLCJhIjoiY2psZm8ybnFnMHl4NDNwcG16eGFmMTdwaCJ9.2xYdBHCpcf5cdap8BvhVgQ' });

