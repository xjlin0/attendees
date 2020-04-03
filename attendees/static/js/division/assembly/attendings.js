Attendees.attendings = {
  init: () => {

    console.log("attendees/static/js/division/assembly/attendings.js");

    Attendees.attendings.setDefaults();

    $('.basic-multiple').select2({
      theme: 'bootstrap4',
    });

    $('div.for-select-all').on('click', 'input.select-all', e => Attendees.utilities.toggleSelect2All(e, 'select.search-filters'));

    $("div.attendings").dxDataGrid(Attendees.attendings.attendingsFormats);

    $('form.attendings-filter').on('change', 'select.search-filters', Attendees.utilities.debounce(250, Attendees.attendings.fetchAttendings));
  },

  fetchAttendings: (event) => {
    Attendees.utilities.alterCheckBoxAndValidations(event, 'input.select-all');

    let finalUrl = null;
    const $optionForm = $(event.delegateTarget);
    const $meetsSelectBox = $optionForm.find('select.filter-meets');
    const $charactersSelectBox = $optionForm.find('select.filter-characters');
    const meets = $meetsSelectBox.val() || [];
    const characters = $charactersSelectBox.val() || [];

    if (meets.length && characters.length) {
      const url = $('div.attendings').data('attendings-endpoint');
      const searchParams = new URLSearchParams();
      meets.forEach(meet => { searchParams.append('meets', meet)});
      characters.forEach(character => { searchParams.append('characters', character)});
      finalUrl = `${url}?${searchParams.toString()}`
    }

    $("div.attendings")
      .dxDataGrid("instance")
      .option("dataSource", finalUrl);

  },

  attendingsFormats: {
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
//      {
//        dataField: "gathering",
//        lookup: {
//            valueExpr: "id",
//            displayExpr: "gathering_label",
//            dataSource: {
//                store: new DevExpress.data.CustomStore({
//                    key: "id",
//                    load: () => {
//                      return $.getJSON($('div.attendances').data('gatherings-endpoint'), {meets: $('select.filter-meets').val()});
//                    },
//                }),
//            },
//        }
//      },
//      {
//        caption: 'Attending (Register)',
//        dataField: "attending",
//        lookup: {
//            valueExpr: "id",
//            displayExpr: "attending_label",
//            dataSource: {
//                store: new DevExpress.data.CustomStore({
//                    key: "id",
//                    load: () => {
//                      return $.getJSON($('div.attendances').data('attendings-endpoint'), {meets: $('select.filter-meets').val()});
//                    },
//                }),
//            },
//        }
//      },
//      {
//        dataField: "team",
//        lookup: {
//            valueExpr: "id",
//            displayExpr: "display_name",
//            dataSource: {
//                store: new DevExpress.data.CustomStore({
//                    key: "id",
//                    load: () => {
//                      return $.getJSON($('div.attendances').data('teams-endpoint'), {meets: $('select.filter-meets').val()});
//                    },
//                }),
//            },
//        }
//      },
//      {
//        dataField: "character",
//        lookup: {
//            valueExpr: "id",
//            displayExpr: "display_name",
//            dataSource: {
//                store: new DevExpress.data.CustomStore({
//                    key: "id",
//                    load: () => {
//                      return $.getJSON($('div.attendances').data('characters-endpoint'));
//                    },
//                }),
//            },
//        }
//      },
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
    const urlParams = new URLSearchParams(window.location.search);
    const characters = urlParams.getAll('characters');
    document.getElementById('filter-characters').value = characters;

    document.getElementById('filter-meets').value = [];
  },
}

$(document).ready(() => {
  Attendees.attendings.init();
});
