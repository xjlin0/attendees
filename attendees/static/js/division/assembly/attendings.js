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
    Attendees.utilities.alterCheckBoxAndValidations(event.currentTarget, 'input.select-all');

    let finalUrl = null;
    const $optionForm = $(event.delegateTarget);
    const $meetsSelectBox = $optionForm.find('select.filter-meets');
    const $charactersSelectBox = $optionForm.find('select.filter-characters');
    const meets = $meetsSelectBox.val() || [];
    const characters = $charactersSelectBox.val() || [];

    if (meets.length && characters.length) {
      const url = $('div.attendings').data('attendings-endpoint');
      const searchParams = new URLSearchParams();
      meets.forEach(meet => { searchParams.append('meets[]', meet)});
      characters.forEach(character => { searchParams.append('characters[]', character)});
      finalUrl = `${url}?${searchParams.toString()}`
    }

    $("div.attendings")
      .dxDataGrid("instance")
      .option("dataSource", finalUrl);

  },

  attendingsFormats: {
    dataSource: null,
//    height: '80%',
    filterRow: { visible: true },  //filter doesn't work with fields with calculateDisplayValue yet
    searchPanel: { visible: true },   //search doesn't work with fields with calculateDisplayValue yet
    allowColumnReordering: true,
    columnAutoWidth: true,
    allowColumnResizing: true,
    columnResizingMode: 'nextColumn',
    rowAlternationEnabled: true,
    hoverStateEnabled: true,
    loadPanel: true,
    wordWrapEnabled: false,
    grouping: {
      autoExpandAll: true,
    },
    groupPanel: {
      visible: "auto",
    },
    columnChooser: {
      enabled: true,
      mode: "select",
    },
    columnFixing: {
      enabled: true
    },
    onCellPrepared: e => e.rowType === "header" && e.column.dataHtmlTitle && e.cellElement.attr("title", e.column.dataHtmlTitle),
    // compatible with cellHintEnabled (hint didn't work) and make entire column shows title. https://supportcenter.devexpress.com/ticket/details/t541796
//    scrolling: {
//            mode: "virtual",
//    },
    columns: [
      {
        dataField: "id",
        allowGrouping: false,
      },
      {
        caption: 'Attendee',
        allowFixing: true,
        dataField: "attendee",
        calculateCellValue: rowData => rowData.attendee.display_label,
      },
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
      {
        dataField: "meet",
        dataType: "string",
        groupIndex: 0,
      },
      {
        dataField: "character",
        caption: 'role',
        dataType: "string",
      },
      {
        caption: 'grade',
        dataField: "infos.grade",
        calculateCellValue: rowData => rowData.infos.grade,
      },
      {
        caption: 'Birthday',
        dataHtmlTitle: "Could be real or estimated, depends on user inputs",
        dataField: "attendee",
        calculateCellValue: rowData => {
          const date = rowData.attendee.actual_birthday ? rowData.attendee.actual_birthday : rowData.attendee.estimated_birthday;
          return date ? new Date(date).toLocaleDateString() : null;
        },
      },
      {
        caption: 'Age',
        dataHtmlTitle: "Could be real or estimated, depends on user inputs",
        dataField: "attendee",
        dataType: "number",
        calculateCellValue: rowData => {
          const oneYear = 31557600 * 1000;
          const date = rowData.attendee.actual_birthday ? rowData.attendee.actual_birthday : rowData.attendee.estimated_birthday;
          return date ? Math.round((new Date() - new Date(date))/oneYear): rowData.age;
        },
      },
      {
        caption: "Parents/Caregivers",
        dataField: "attendee.parents_notifiers_names",
        calculateCellValue: rowData => rowData.attendee.parents_notifiers_names,
      },
      {
        caption: "Self emails",
        dataField: "attendee.self_email_addresses",
//        width: '15%',
        calculateCellValue: rowData => rowData.attendee.self_email_addresses,
      },
      {
        caption: "Parents emails",
        dataField: "attendee.caregiver_email_addresses",
        calculateCellValue: rowData => rowData.attendee.caregiver_email_addresses,
      },
      {
        caption: "Self phones",
        dataField: "attendee.self_phone_numbers",
        calculateCellValue: rowData => rowData.attendee.self_phone_numbers,
      },
      {
        caption: "Parents phones",
        dataField: "attendee.caregiver_phone_numbers",
        calculateCellValue: rowData => rowData.attendee.caregiver_phone_numbers,
      },
      {
        caption: 'allergy',
        dataField: "attendee.infos.allergy",
        calculateCellValue: rowData => rowData.attendee.infos.allergy,
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
