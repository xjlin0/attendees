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
//          dataSource: "/1_cfcc-hayward/occasions/api/gatherings",
          dataSource: [{"id":1,"created":"2020-02-08T15:23:16.982000-08:00","modified":"2020-02-08T15:23:16.982000-08:00","meet":1,"start":"2020-02-09T10:00:00-08:00","finish":"2020-02-09T12:00:00-08:00","display_name":"02/09/2020","link":null,"occurrence":null,"site_type":31,"site_id":1},{"id":2,"created":"2020-02-16T20:01:15.902000-08:00","modified":"2020-02-16T20:01:15.902000-08:00","meet":1,"start":"2020-02-16T10:00:00-08:00","finish":"2020-02-16T12:00:00-08:00","display_name":"02/16/2020","link":null,"occurrence":null,"site_type":32,"site_id":1},{"id":4,"created":"2020-02-17T07:09:03.335000-08:00","modified":"2020-02-17T07:09:03.335000-08:00","meet":2,"start":"2020-02-09T10:00:00-08:00","finish":"2020-02-09T12:00:00-08:00","display_name":"02/09/2020","link":null,"occurrence":null,"site_type":30,"site_id":1},{"id":3,"created":"2020-02-17T07:01:37.575000-08:00","modified":"2020-02-17T07:01:37.575000-08:00","meet":3,"start":"2020-01-10T09:00:00-08:00","finish":"2020-01-10T12:00:00-08:00","display_name":"01/10/2020","link":null,"occurrence":null,"site_type":30,"site_id":2},{"id":5,"created":"2020-02-17T18:32:54.537000-08:00","modified":"2020-02-17T18:37:42.317000-08:00","meet":4,"start":"2020-02-17T00:00:00-08:00","finish":"9999-12-29T00:00:01-08:00","display_name":"forever","link":null,"occurrence":null,"site_type":29,"site_id":2}],
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
