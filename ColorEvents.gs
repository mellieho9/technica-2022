function ColorEvents() {
 
  var today = new Date();
  var nextmonth = new Date();
  nextmonth.setDate(nextmonth.getDate() + 31);
  Logger.log(today + " " + nextmonth);
 
  var calendars = CalendarApp.getAllOwnedCalendars();
  Logger.log("found number of calendars: " + calendars.length);
 
  for (var i=0; i<calendars.length; i++) {
    var calendar = calendars[i];
    var events = calendar.getEvents(today, nextmonth);
    for (var j=0; j<events.length; j++) {
      var e = events[j];
      var location = e.getLocation();
     if (location.includes("IRB0324")) {
        e.setColor(CalendarApp.EventColor.CYAN);
      }
     else if (location.includes("CSI3120")) {
        e.setColor(CalendarApp.EventColor.PALE_BLUE);
      }
      else if (location.includes("CSI2107")) {
        e.setColor(CalendarApp.EventColor.PALE_RED);
      }
      else if (location.includes("CSI1122")) {
        e.setColor(CalendarApp.EventColor.YELLOW);
      }
    }
  }
}
