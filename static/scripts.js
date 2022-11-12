$(function () {
  $('btnLogin').click(function () {

    $.ajax({
      url: '/login',
      data: $('form').serialize(),
      type: 'POST',
      succes: function (response) {
        console.log(response);
      },
      error: function (error) {
        console.log(error);
      }
    });

  });
});
