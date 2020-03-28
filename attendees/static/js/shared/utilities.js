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

  testArraysEqualAfterSort : (a, b) => {
    a = Array.isArray(a) ? a.sort() : [];
    b = Array.isArray(b) ? b.sort() : [];
    return a.length === b.length && a.every((el, ix) => el === b[ix]);
  }, // https://stackoverflow.com/a/39967517/4257237
}

$(document).ready(() => {
  Attendees.utilities.init();
});
