/*

Script file you need to run on your local Google App Script to color code the newly generated schedule

*/
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
      var title = e.getLocation();
      Logger.log(title);
     if (title === "CMSC131_Lect" || title === "CMSC131_Disc") {
        e.setColor(CalendarApp.EventColor.PALE_GREEN);
      }
     else if (title === "CMSC132_Lect" || title === "CMSC132_Disc") {
        e.setColor(CalendarApp.EventColor.PALE_BLUE);
      }
      else if (title === "CMSC216_Lect" || title === "CMSC216_Disc") {
        e.setColor(CalendarApp.EventColor.PALE_RED);
      }
      else if (title === "CMSC250_Lect" || title === "CMSC250_Disc"|| title === "CMSC250H_Lect" || title === "CMSC250H_Disc") {
        e.setColor(CalendarApp.EventColor.MAUVE);
      }
      else if (title === "CMSC330_Lect" || title === "CMSC330_Disc") {
        e.setColor(CalendarApp.EventColor.BLUE);
      }
      else if (title === "CMSC401") {
        e.setColor(CalendarApp.EventColor.ORANGE);
      }
      else if (title === "MATH140_Lect" || title === "MATH140_Disc") {
        e.setColor(CalendarApp.EventColor.YELLOW);
      }
    }
  }
}

