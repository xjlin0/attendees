console.log("assets/js/index.js 1 in index.js!!567800000");
(($, Attendees) => {
  if (typeof Attendees === 'undefined') window.Attendees = {};
  console.log("attendees/static/js/shared/index.js 4");
  const timeZoneName = Intl.DateTimeFormat().resolvedOptions().timeZone;
  document.cookie = 'timezone=' + encodeURIComponent(timeZoneName) + '; path=/';
  console.log('jQ version: ', window.jQuery().jquery);
})(window.jQuery, window.Attendees); // https://stackoverflow.com/a/18315393
