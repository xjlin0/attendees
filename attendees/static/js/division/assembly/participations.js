Attendees.leaderIndex = {
  init: () => {

    console.log("attendees/static/js/division/assembly/participations.js");
    Attendees.leaderIndex.setDefaults();

    $('.basic-multiple').select2({
      placeholder: "Nothing selected",
    });

//    $('form.participations-filter').on('change', 'input, select', Attendees.utilities.debounce(250, Attendees.leaderIndex.fetchParticipations));
//Attendees.leaderIndex.loadDataGrid();
    $("div#gridContainer").dxDataGrid({dataSource: "/1_cfcc-hayward/occasions/api/children_ministry/kid_regular/participations/"});
  },

  loadDataGrid: () => {
    $("div#devExtreme").dxButton({
      text: "Test",
      onClick: (args) => {
        console.log("clicked!");
        customers = [
          {
            ID: 211,
            CompanyName: "Super Mart of the West",
            Address: "702 SW 8th Street",
            City: "Bentonville",
            State: "Arkansas",
            Zipcode: 72716,
            Phone: "(800) 555-2797",
            Fax: "(800) 555-2171"
          }
        ];
        $("#gridContainer")
          .dxDataGrid("instance")
          .refresh();
      }
    });
    $("div#gridContainer").dxDataGrid({
      dataSource: {
        key: "ID",
        load: () => { // https://js.devexpress.com/Documentation/Guide/Widgets/DataGrid/Data_Binding/JSON_Data/
          return [
                    {
                      ID: 1,
                      CompanyName: "Super Mart of the West",
                      Address: "702 SW 8th Street",
                      City: "Bentonville",
                      State: "Arkansas",
                      Zipcode: 72716,
                      Phone: "(800) 555-2797",
                      Fax: "(800) 555-2171",
                      Website: "http://www.nowebsitesupermart.com"
                    },
                    {
                      ID: 2,
                      CompanyName: "Electronics Depot",
                      Address: "2455 Paces Ferry Road NW",
                      City: "Atlanta",
                      State: "Georgia",
                      Zipcode: 30339,
                      Phone: "(800) 595-3232",
                      Fax: "(800) 595-3231",
                      Website: "http://www.nowebsitedepot.com"
                    }
                  ];
        }
      },
      columns: ["CompanyName", "City", "State", "Phone", "Fax"],
      showBorders: true
    });
  },


  participationsFormats: {
    dataSource: $('div.gridContainer').data('url'),
    // filterRow: { visible: true },  //filter doesn't work with fields with calculateDisplayValue yet
    searchPanel: { visible: true },
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
