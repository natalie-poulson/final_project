console.log('hello')

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