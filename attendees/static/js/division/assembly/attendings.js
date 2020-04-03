Attendees.attendings = {
  init: () => {

    console.log("attendees/static/js/division/assembly/attendings.js");

    $('.basic-multiple').select2({
      theme: 'bootstrap4',
    });
  },
}

$(document).ready(() => {
  Attendees.attendings.init();
});
