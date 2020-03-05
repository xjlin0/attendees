console.log("assets/js/index.js 1 in index!!!!");
(($, Attendees) => {
  if (typeof Attendees === 'undefined') window.Attendees = {};
  console.log("attendees/static/js/shared/base.js");
  const timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone;
  document.cookie = 'timezone=' + encodeURIComponent(timeZoneName) + '; path=/';
})(window.jQuery, window.Attendees); // https://stackoverflow.com/a/18315393
