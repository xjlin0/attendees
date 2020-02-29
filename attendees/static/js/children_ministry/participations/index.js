Attendees.leaderIndex = {
  init: () => {
    Attendees.leaderIndex.setDefaults();

    $('.basic-multiple').select2({
      placeholder: "Nothing selected",
    });

    $('form.participations-filter').on('change', 'input, select', Attendees.utilities.debounce(250, Attendees.leaderIndex.fetchParticipations));

    $("#gridContainer").dxDataGrid(Attendees.leaderIndex.participationsFormats);
  },

  participationsFormats: {
    dataSource: "/1_cfcc-hayward/occasions/api/participations/",

    rowAlternationEnabled: true,
    hoverStateEnabled: true,
    loadPanel: true,
    columns: [
      "id",
      {
        dataField: "gathering",
        lookup: {
          dataSource: "/1_cfcc-hayward/occasions/api/gatherings",
          displayExpr: "display_name",
          valueExpr: "id",
        }
      },
      {
        dataField: "modified",
        dataType: "datetime"
      },
    ],
  },

  fetchParticipations: (event) => {
    const $optionForm=$(event.delegateTarget);
    const $resultElement=$('div.participations');
    const chosenOptions={
      start: $optionForm.find('input.filter-start-date').val(),
      finish: $optionForm.find('input.filter-finish-date').val(),
      meets: $optionForm.find('select.filter-meets').val(),
    };

    if (chosenOptions.meets) {
    $resultElement.html('<h3> Fetching data .... </h3>');
      $.ajax
      ({
        url      : $optionForm.data('url'),
        data     : chosenOptions,
        success  : (response) => {
                     $resultElement.html(response)
                   },
        error    : (response) => {
                     $resultElement.html('There are some errors: ', response);
                   },
      });
    } else {
      $resultElement.html($resultElement.data('default'));
    }
  },

  setDefaults: () => {
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
