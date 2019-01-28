$(document).ready(function(){

    var $withdrawNoty = $('#with-success');
    if ($withdrawNoty.length){
        Swal(
            $withdrawNoty.text(),
            'You will get your Bitcoin asap to your Bitcoin wallet',
            'success'
          );
    }

    var $withdrawDeniedNoty = $('#enough-balance');
    if ($withdrawDeniedNoty.length){
        Swal(
            'Withdrawal denied',
            $withdrawDeniedNoty.text(),
            'error'
          );
    }

    var $verifyError = $('#recaptcha-fail');
    if ($verifyError.length){
        Swal(
            'Whoops! That\'s an error!',
            'We couldn\'t verify that was a legimate move',
            'error'
          )
    }

    var $withdrawalError = $('#with-denied');
    if ($withdrawalError.length){
        Swal(
            $withdrawalError.text(),
            'Please try again later',
            'error'
          );
    }


});