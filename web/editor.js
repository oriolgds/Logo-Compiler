// SQL keywords
var keywords = ["SELECT","FROM","WHERE","LIKE","BETWEEN","NOT LIKE","FALSE","NULL","FROM","TRUE","NOT IN"];
// Keyup event
$("#editor").on("keyup", function(e){
  // Space key pressed
  if (e.keyCode == 32){
    var newHTML = "";
    // Loop through words
    $(this).text().replace(/[\s]+/g, " ").trim().split(" ").forEach(function(val){
      // If word is statement
      if (keywords.indexOf(val.trim().toUpperCase()) > -1)
        newHTML += "<span class='statement'>" + val + "&nbsp;</span>";
      else
        newHTML += "<span class='other'>" + val + "&nbsp;</span>"; 
    });
    $(this).html(newHTML);

    // Set cursor postion to end of text
    var child = $(this).children();
    var range = document.createRange();
    var sel = window.getSelection();
    range.setStart(child[child.length-1], 1);
    range.collapse(true);
    sel.removeAllRanges();
    sel.addRange(range);
    this.focus();
  }
});