$(document).ready(function(){

    var $claimNoty = $('#notify-claim-msg');
    if ($claimNoty.length){
        Swal(
            $claimNoty.text(),
            'Wait a bit and get your next free Bitcoin',
            'success'
          )
    }

    var $verifyError = $('#recaptcha-fail');
    if ($verifyError.length){
        Swal(
            'Whoops! That\'s an error!',
            'We couldn\'t verify that was a legimate move',
            'error'
          )
    }

    var $claimError = $('#notify-claim-warning');
    if ($claimError.length){
        Swal(
            $claimError.text(),
          )
    }


});