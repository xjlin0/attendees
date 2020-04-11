Attendees.organizationAttendances = {
  init: () => {

    console.log("attendees/static/js/coworkers/organization_attendances.js");

    Attendees.organizationAttendances.setDefaults();
    Attendees.organizationAttendances.initTempusdominus();
    $('.basic-multiple').select2({
      theme: 'bootstrap4',
    });
    $('form.organization-attendances-filter, div.datetimepickers').on('change, change.datetimepicker', 'select.search-filters, div.datetimepickers', Attendees.utilities.debounce(250, Attendees.organizationAttendances.fetchAttendances));
    $('div.for-select-all').on('click', 'input.select-all', e => Attendees.utilities.toggleSelect2All(e, 'select.search-filters'));
    $("div.organization-attendances").dxDataGrid(Attendees.organizationAttendances.attendancesFormats);
    Attendees.utilities.alterCheckBoxAndValidations(document.querySelector('select.filter-meets'), 'input.select-all');
  },

  fetchAttendances: (event) => {
    Attendees.utilities.alterCheckBoxAndValidations(event.currentTarget, 'input.select-all');

    let finalUrl = null;
    const $optionForm = $(event.delegateTarget);
    const $meetsSelectBox = $optionForm.find('select.filter-meets');
    const meets = $meetsSelectBox.val() || [];
    const startDate = $optionForm.find('input.filter-start-date').val();
    const endDate = $optionForm.find('input.filter-finish-date').val();

    if (startDate && endDate && meets.length) {
      const start = (new Date($optionForm.find('input.filter-start-date').val())).toISOString();
      const finish = (new Date($optionForm.find('input.filter-finish-date').val())).toISOString();
      const url = $('div.organization-attendances').data('attendances-endpoint');
      const searchParams = new URLSearchParams({start: start, finish: finish});
      meets.forEach(meet => { searchParams.append('meets', meet)});
      finalUrl = `${url}?${searchParams.toString()}`
    }

    $("div.organization-attendances")
      .dxDataGrid("instance")
      .option("dataSource", finalUrl);
  }, // Getting JSON from DRF upon user selecting meet(s)

  attendancesFormats: {
    onInitialized: () => {console.log('need to call fetchAttendances()!')},
    dataSource: null,
    filterRow: { visible: true },  //filter doesn't work with fields with calculateDisplayValue yet
    searchPanel: { visible: true },   //search doesn't work with fields with calculateDisplayValue yet
    allowColumnReordering: true,
    columnAutoWidth: true,
    allowColumnResizing: true,
    columnResizingMode: 'nextColumn',
    rowAlternationEnabled: true,
    hoverStateEnabled: true,
    loadPanel: true,
    grouping: {
        autoExpandAll: true,
    },
    groupPanel: {
        visible: "auto",
    },
    columns: [
      {
        dataField: "id",
        allowGrouping: false,
      },
      {
        dataField: "gathering",
        groupIndex: 0,
        lookup: {
            valueExpr: "id",
            displayExpr: "gathering_label",
            dataSource: {
                store: new DevExpress.data.CustomStore({
                    key: "id",
                    load: () => {
                      return $.getJSON($('div.organization-attendances').data('gatherings-endpoint'), {meets: $('select.filter-meets').val()});
                    },
                }),
            },
        }
      },
      {
        caption: 'Attending (Register)',
        dataField: "attending",
        lookup: {
            valueExpr: "id",
            displayExpr: "attending_label",
            dataSource: {
                store: new DevExpress.data.CustomStore({
                    key: "id",
                    load: () => {
                      return $.getJSON($('div.organization-attendances').data('attendings-endpoint'), {meets: $('select.filter-meets').val()});
                    },
                }),
            },
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
                      return $.getJSON($('div.organization-attendances').data('teams-endpoint'), {meets: $('select.filter-meets').val()});
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
                      return $.getJSON($('div.organization-attendances').data('characters-endpoint'));
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

  setDefaults: () => {
    const locale = "en-us"
    const dateOptions = { day: '2-digit', month: '2-digit', year: 'numeric' };
    const timeOptions = { hour12: true, hour: '2-digit', minute:'2-digit' };
    const defaultFilterStartDate = new Date();
    const defaultFilterFinishDate = new Date();
    defaultFilterStartDate.setMonth(defaultFilterStartDate.getMonth() - 1);
    defaultFilterFinishDate.setMonth(defaultFilterFinishDate.getMonth() + 1);
    $('input.filter-start-date').val(defaultFilterStartDate.toLocaleDateString(locale, dateOptions) + ' ' + defaultFilterStartDate.toLocaleTimeString(locale, timeOptions));
    $('input.filter-finish-date').val(defaultFilterFinishDate.toLocaleDateString(locale, dateOptions) + ' ' + defaultFilterFinishDate.toLocaleTimeString(locale, timeOptions));
//    document.getElementById('filter-meets').value = [];
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
  Attendees.organizationAttendances.init();
});
