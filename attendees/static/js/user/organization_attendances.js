Attendees.organizationAttendances = {
  init: () => {

    console.log("attendees/static/js/user/organization_attendances.js");
//    $("div.attendances").dxDataGrid(Attendees.organizationAttendances.attendancesFormats);
  },

  attendancesFormats: {
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
                      return $.getJSON($('div.attendances').data('gatherings-endpoint'), {meets: $('select.filter-meets').val()});
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
                      return $.getJSON($('div.attendances').data('attendings-endpoint'), {meets: $('select.filter-meets').val()});
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
                      return $.getJSON($('div.attendances').data('teams-endpoint'), {meets: $('select.filter-meets').val()});
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
                      return $.getJSON($('div.attendances').data('characters-endpoint'));
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
}

$(document).ready(() => {
  Attendees.organizationAttendances.init();
});
