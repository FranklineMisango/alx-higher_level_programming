const url = "https://fourtonfish.com/hellosalut/?lang=fr";

$('document').ready(function () {
    $.get(url, function (data) {
      $('DIV#hello').text(data.hello);
    });
});
