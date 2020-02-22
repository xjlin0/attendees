Attendees.leaderIndex = {
  init: () => {
    console.log("attendees/static/js/children_ministry/participations/leader_index.js");
    Attendees.leaderIndex.set_defaults();
    $('button.load-participations').on('click', Attendees.leaderIndex.fetch_participations)
  },

  fetch_participations: () => {
    console.log("loading participations button clicked");

    $.ajax
    ({
      url      : "/1_cfcc-hayward/occasions/children_ministry/participations/leaders/?hi=5",
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
