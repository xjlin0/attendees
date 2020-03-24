Attendees.leaderIndex = {
  init: () => {

    console.log("attendees/static/js/division/assembly/participations.js");
    Attendees.leaderIndex.setDefaults();
    Attendees.leaderIndex.initTempusdominus();
    $('.basic-multiple').select2({
      placeholder: "Nothing selected",
    });

    $('form.participations-filter').on('change', 'input.text, select', Attendees.utilities.debounce(250, Attendees.leaderIndex.fetchParticipations));

    $("div.participatingLeaders").dxDataGrid(Attendees.leaderIndex.participationsFormats);
  },



  participationsFormats: {
    dataSource: null,
    // filterRow: { visible: true },  //filter doesn't work with fields with calculateDisplayValue yet
    searchPanel: { visible: true },   //search doesn't work with fields with calculateDisplayValue yet
    allowColumnReordering: true,
    columnAutoWidth: true,
    allowColumnResizing: true,
    columnResizingMode: 'nextColumn',
    rowAlternationEnabled: true,
    hoverStateEnabled: true,
    loadPanel: true,
    grouping: {
        contextMenuEnabled: true,
    },
    groupPanel: {
        visible: true   // or "auto"
    },
    columns: [
      {
        dataField: "id",
        allowGrouping: false,
      },
      { // https://js.devexpress.com/Documentation/Guide/Widgets/DataGrid/Enhance_Performance_on_Large_Datasets/#Lookup_Optimization
        caption: "Gathering",
        allowFiltering: false,
        calculateDisplayValue: "gathering_label",
        dataField: "gathering",
        lookup: {
            valueExpr: "id",
            displayExpr: "display_name",
            dataSource: {
                store: {
                    key: "id"
                }
            }
        }
      },
      {
        caption: "Attending-Parent",
        allowFiltering: false,
        calculateDisplayValue: "attending_label",
        dataField: "attending",
        lookup: {
            valueExpr: "id",
            displayExpr: "display_name",
            dataSource: {
                store: {
                    key: "id"
                }
            }
        }
      },
      {
        caption: "Team",
        allowFiltering: false,
        calculateDisplayValue: "team_label",
        dataField: "team",
        lookup: {
            valueExpr: "id",
            displayExpr: "display_name",
            dataSource: {
                store: {
                    key: "id"
                }
            }
        }
      },
      {
        caption: "Character",
        calculateDisplayValue: "character_label",
        dataField: "character",
        allowFiltering: false,
//        lookup: {
//            valueExpr: "id",
//            displayExpr: "display_name",
//            dataSource: {
//                store: {
//                    key: "id"
//                }
//            }
//        }
      },
      {
        dataField: "category",
        dataType: "string"
      },
      {
        dataField: "modified",
        allowGrouping: false,
        dataType: "datetime"
      },
    ],
  },


  fetchParticipations: (event) => {
    let finalUrl = null;
    const $optionForm = $(event.delegateTarget);
    const meets = $optionForm.find('select.filter-meets').val();
    const chosenOptions = {
      start: $optionForm.find('input.filter-start-date') && moment($optionForm.find('input.filter-start-date').val()).format('YYYY-MM-DDTHH:MMZ'),
      finish: $optionForm.find('input.filter-finish-date') && moment($optionForm.find('input.filter-finish-date').val()).format('YYYY-MM-DDTHH:MMZ'),
    };

    if (chosenOptions.start && chosenOptions.finish && Array.isArray(meets) && meets.length) {
      const url = $('div.participatingLeaders').data('url');
      const searchParams = new URLSearchParams(chosenOptions);
      meets.forEach(meet => { searchParams.append('meets', meet)});
      finalUrl = `${url}?${searchParams.toString()}`
    }

    $("div.participatingLeaders")
      .dxDataGrid("instance")
      .option("dataSource", finalUrl);
  }, // Getting JSON from DRF upon user selecting meet(s)

  fetchParticipationsOld: (event) => {
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
  }, // Getting html from Django upon user selecting meet(s)

  setDefaults: () => {
    const defaultFilterStartDate = new Date();
    const defaultFilterFinishDate = new Date();
    defaultFilterStartDate.setMonth(defaultFilterStartDate.getMonth() - 3);
    defaultFilterFinishDate.setMonth(defaultFilterFinishDate.getMonth() + 6);
    document.getElementById('filter-start-date').value = defaultFilterStartDate.toISOString().substring(0, 10);
    document.getElementById('filter-finish-date').value = defaultFilterFinishDate.toISOString().substring(0, 10);
    document.getElementById('filter-meets').value = [];
  },

  initTempusdominus: () => {
    $.fn.datetimepicker.Constructor.Default = $.extend({},
                $.fn.datetimepicker.Constructor.Default,
                { icons:
                        { time: 'fas fa-clock',
                            date: 'fas fa-calendar',
                            up: 'fas fa-arrow-up',
                            down: 'fas fa-arrow-down',
                            previous: 'fas fa-arrow-circle-left',
                            next: 'fas fa-arrow-circle-right',
                            today: 'far fa-calendar-check-o',
                            clear: 'fas fa-trash',
                            close: 'far fa-times' } });
  },
}

$(document).ready(() => {
  Attendees.leaderIndex.init();
});
