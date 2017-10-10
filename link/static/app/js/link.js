$(document).ready(function() {

  $('div').scrollspy({ target: '#screen' });
  $('body').scrollspy({ target: '#navbar-example' })

  $('[data-spy="scroll"]').each(function () {
    var $spy = $(this).scrollspy('refresh')
  });
})
