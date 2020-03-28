Attendees.leaderIndex = {
  init: () => {

    console.log("attendees/static/js/division/assembly/participations.js");
    Attendees.leaderIndex.setDefaults();
    Attendees.leaderIndex.initTempusdominus();
    $('.basic-multiple').select2({
      theme: 'bootstrap4',
    });

    $('form.participations-filter, div.datetimepickers').on('change, change.datetimepicker', 'select.filter-meets, div.datetimepickers', Attendees.utilities.debounce(250, Attendees.leaderIndex.fetchParticipations));
    $('div.for-select-all').on('click', 'input.select-all', Attendees.leaderIndex.toggleSelectAll);
    $("div.participatingLeaders").dxDataGrid(Attendees.leaderIndex.participationsFormats);
  },

  toggleSelectAll: (event) => {
     const $select2Input = $(event.delegateTarget).find('select.select2');
     const $checkAllBox = $(event.currentTarget);
     const options = $checkAllBox.is(':checked') ? $select2Input.data('all-options') : [];
     $select2Input.val(options).trigger('change');
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
      {
        dataField: "gathering",
        lookup: {
            valueExpr: "id",
            displayExpr: "display_name",
            dataSource: {
                store: new DevExpress.data.CustomStore({
                    key: "id",
                    load: () => {
                      return $.getJSON($('div.participatingLeaders').data('gatherings-endpoint'));
                    },
                }),
            },
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
        dataField: "team",
        lookup: {
            valueExpr: "id",
            displayExpr: "display_name",
            dataSource: {
                store: new DevExpress.data.CustomStore({
                    key: "id",
                    load: () => {
                      return $.getJSON($('div.participatingLeaders').data('teams-endpoint'));
                    },
                }),
            },
        }
      },
      {
        dataField: "character",
        lookup: {
            valueExpr: "id",
            displayExpr: "display_name",
            dataSource: {
                store: new DevExpress.data.CustomStore({
                    key: "id",
                    load: () => {
                      return $.getJSON($('div.participatingLeaders').data('characters-endpoint'));
                    },
                }),
            },
        }
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
    const $meetsSelectBox = $optionForm.find('select.filter-meets');
    const $checkAllBox = $optionForm.find('input.select-all')
    const allOptions = $meetsSelectBox.data('all-options');
    const meets = $meetsSelectBox.val() || [];
    const startDate = $optionForm.find('input.filter-start-date').val();
    const endDate = $optionForm.find('input.filter-finish-date').val();

    if (meets.length) {
      $meetsSelectBox.removeClass('is-invalid');
    } else {
      $meetsSelectBox.addClass('is-invalid');
    }

    $checkAllBox.prop('checked', Attendees.utilities.testArraysEqualAfterSort(meets, allOptions));

    if (startDate && endDate && meets.length) {
      const start = (new Date($optionForm.find('input.filter-start-date').val())).toISOString();
      const finish = (new Date($optionForm.find('input.filter-finish-date').val())).toISOString();
      const url = $('div.participatingLeaders').data('participations-endpoint');
      const searchParams = new URLSearchParams({start: start, finish: finish});
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
    const locale = "en-us"
    const dateOptions = { day: '2-digit', month: '2-digit', year: 'numeric' };
    const timeOptions = { hour12: true, hour: '2-digit', minute:'2-digit' };
    const defaultFilterStartDate = new Date();
    const defaultFilterFinishDate = new Date();
    defaultFilterStartDate.setMonth(defaultFilterStartDate.getMonth() - 3);
    defaultFilterFinishDate.setMonth(defaultFilterFinishDate.getMonth() + 6);
    $('input.filter-start-date').val(defaultFilterStartDate.toLocaleDateString(locale, dateOptions) + ' ' + defaultFilterStartDate.toLocaleTimeString(locale, timeOptions));
    $('input.filter-finish-date').val(defaultFilterFinishDate.toLocaleDateString(locale, dateOptions) + ' ' + defaultFilterFinishDate.toLocaleTimeString(locale, timeOptions));
    document.getElementById('filter-meets').value = [];
  }, // https://stackoverflow.com/a/50000889

  initTempusdominus: () => {
    $.fn.datetimepicker.Constructor.Default = $.extend({},
        $.fn.datetimepicker.Constructor.Default, {
            icons: {
                time: 'fas fa-clock',
                date: 'fas fa-calendar',
                up: 'fas fa-arrow-up',
                down: 'fas fa-arrow-down',
                previous: 'fas fa-arrow-circle-left',
                next: 'fas fa-arrow-circle-right',
                today: 'far fa-calendar-check-o',
                clear: 'fas fa-trash',
                close: 'far fa-times',
            }
        }
    );
  },
}

$(document).ready(() => {
  Attendees.leaderIndex.init();
});
