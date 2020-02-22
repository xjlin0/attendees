Attendees.leaderIndex = {
  init: () => {
    console.log("attendees/static/js/children_ministry/participations/leader_index.js");
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
      error  : function(response){console.log('hi jack here is error response: ', response) }
    });
  },
}

$(document).ready(() => {
  Attendees.leaderIndex.init();
});
