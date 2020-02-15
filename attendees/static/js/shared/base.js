(($, Attendee) => {
  if (typeof Attendee === 'undefined') window.Attendee = {};
  console.log("attendees/attendees/static/js/shared/base.js");
  const timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone;
  document.cookie = 'timezone=' + encodeURIComponent(timeZoneName) + '; path=/';
})(window.jQuery, window.Attendee); // https://stackoverflow.com/a/18315393
