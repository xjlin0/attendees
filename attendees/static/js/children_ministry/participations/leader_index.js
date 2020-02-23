Attendees.leaderIndex = {
  init: () => {
    Attendees.leaderIndex.set_defaults();

    $('.js-example-basic-multiple').select2({
      placeholder: "Nothing selected",
    });

    $('form.participations-filter').on('change', 'input, select', Attendees.leaderIndex.fetch_participations);
  },

  fetch_participations: (event) => {
    const $optionForm=$(event.delegateTarget);
    const chosenOptions={
      start: $optionForm.find('input.filter-start-date').val(),
      finish: $optionForm.find('input.filter-finish-date').val(),
      meets: $optionForm.find('select.filter-meets').val(),
    };

    $.ajax
    ({
      url      : $optionForm.data('url'),
      data     : chosenOptions,
      success  : function(response){
        console.log('hi here is success response: ', response);
        $("div.participations").html(response)
        },
      error  : function(response){console.log('hi here is error response: ', response) }
    });
  },

  set_defaults: () => {
    const defaultFilterStartDate = new Date();
    const defaultFilterFinishDate = new Date();
    defaultFilterStartDate.setMonth(defaultFilterStartDate.getMonth() - 3);
    defaultFilterFinishDate.setMonth(defaultFilterFinishDate.getMonth() + 6);
    document.getElementById('filter-start-date').value = defaultFilterStartDate.toISOString().substring(0, 10);
    document.getElementById('filter-finish-date').value = defaultFilterFinishDate.toISOString().substring(0, 10);
  },
}

$(document).ready(() => {
  Attendees.leaderIndex.init();
});
