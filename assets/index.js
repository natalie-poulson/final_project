console.log('what up')

var input = document.getElementById("pac-input");
var autocomplete = new google.maps.places.Autocomplete(input);


$('.post-create-form').on ('submit', function (e) {
    e.preventDefault();
 

    console.log('TEST')
    var place = autocomplete.getPlace();
    console.log(place)
    console.log(place.formatted_address)
    console.log(place.geometry.location.lat())
    console.log(place.geometry.location.lng())

    console.log($('#id_trail').val())
    console.log($('#id_permit').val())
    console.log($('#id_start_date').val())
    console.log($('#id_end_date').val())
    console.log($('#id_completed').val())







})
// $(document).on('submit','#signup-form', function(e){

//     e.preventDefault();
//     var signup_form = $('#signup-form');
//     var action = signup_form.attr('action');
//     var method = signup_form.attr('method');
//     var data_ = signup_form.serialize();

//     console.log (action, method, 'data:',data_)
//     $.ajax({
//         type: method,
//         url: action,
//         data: data_,
//         success: function(data, status) {

//             if ($(data).find('.alert-danger').length > 0) {
//                 $('.modal-content').html(data);
//                 // console.log(data)

//             }else{

//                 console.log('Log In Form Successfuly Summited')
//                 $('#exampleModalCenter').modal('hide')
//                 location.reload(); //Reload the current document page on success

//             }
//         }
//     });

//     return false;
// });