(($, Attendees) => {
  if (typeof Attendees === 'undefined') window.Attendees = {};
  console.log("attendees/static/js/shared/base.js");
  const timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone;
  document.cookie = 'timezone=' + encodeURIComponent(timeZoneName) + '; path=/';

  // $('li.active').removeClass('active');
  $('a[href="' + location.pathname + location.search + '"]').closest('li').addClass('active');
})(window.jQuery, window.Attendees); // https://stackoverflow.com/a/18315393
