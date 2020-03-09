Attendees.utilities = {
  init: () => {
    console.log("attendees/static/js/shared/utilities.js");
  },

  debounce : (delay, fn) => {
    let timer = null;
    return (...arguments) => {
      const context = this,
            args = arguments;

      clearTimeout(timer);
      timer = setTimeout(() => {
        fn.apply(context, args);
      }, delay);
    };
  },
}

$(document).ready(() => {
  Attendees.utilities.init();
});
