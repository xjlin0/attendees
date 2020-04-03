Attendees.attendings = {
  init: () => {

    console.log("attendees/static/js/division/assembly/attendings.js");

    $('.basic-multiple').select2({
      theme: 'bootstrap4',
    });

    $('div.for-select-all').on('click', 'input.select-all', e => Attendees.utilities.toggleSelect2All(e, 'select.search-filters'));
  },
}

$(document).ready(() => {
  Attendees.attendings.init();
});
