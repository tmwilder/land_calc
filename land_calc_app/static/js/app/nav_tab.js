define(['js/lib/jquery-2.0.3.min', '//netdna.bootstrapcdn.com/bootstrap/3.0.3/js/bootstrap.min.js'],
function(jquery){
    $('#nav_tabs a').click(function (e) {
      e.preventDefault();
      $(this).tab('show');
    });

    $("#about_tab").click(function (e){
      $("#calculator").hide();
      $("#about").show();
    });

    $("#calculator_tab").click(function (e){
      $("#about").hide();
      $("#calculator").attr('hide', false);
      $("#calculator").show();
    });

});