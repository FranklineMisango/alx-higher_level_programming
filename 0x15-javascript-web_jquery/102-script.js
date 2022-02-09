const url = 'https://www.fourtonfish.com/hellosalut/hello/';

$(document).ready(function () {
    $('INPUT#btn_translate').click(function () {
      let languageCode = $('INPUT#language_code').val();

      $.get(url, (data) => {
        $('DIV#hello').text(data.query.results.languageCode);
      });
    });
});
