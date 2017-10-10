$(document).ready(function() {

  $('div').scrollspy({ target: '#console' });

  $('[data-spy="scroll"]').each(function () {
    var $spy = $(this).scrollspy('refresh')
  });
})
