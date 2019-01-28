$(document).ready(function(){

    //script for sign up page
    var $startEarningBut = $('#submit_signup');
    var $bitcoinAddress =  $('#bitcoin_address');

    $startEarningBut.prop('disabled', true);

    $bitcoinAddress.on('blur', function(){
        $.ajax({
            type: 'POST',
            url: '/ct65756587',
            data: $('form').serialize(),
            success: function(data){
                if (data.status === false){
                    $startEarningBut.prop('disabled', true);
                    $('#invalid-btc').remove();
                    
                    toastr.options = {
                        "closeButton": false,
                        "debug": false,
                        "newestOnTop": false,
                        "progressBar": false,
                        "positionClass": "toast-bottom-right",
                        "preventDuplicates": false,
                        "onclick": null,
                        "showDuration": "600",
                        "hideDuration": "1000",
                        "timeOut": "5000",
                        "extendedTimeOut": "1000",
                        "showEasing": "swing",
                        "hideEasing": "linear",
                        "showMethod": "fadeIn",
                        "hideMethod": "fadeOut"
                      }
                
                      toastr["error"]("Invalid Bitcoin address.")

                    
                }else{
                    $startEarningBut.prop('disabled', false);
                    $('#invalid-btc').remove();
                };
            }
        });
    });
});