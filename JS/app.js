var menuIcon = document.querySelector(".menuIcon");
var sidebar = document.querySelector(".sidebar");
var container = document.querySelector(".container");

menuIcon.onclick = function() ///sidebar function
{
    sidebar.classList.toggle("smallSidebar");
    container.classList.toggle("largeContainer");
}

function showPopup() // by activating popup you activate its background
{
    var popupBackground = document.getElementById("popupBackground");
    var popup = document.getElementById("popup");

    popupBackground.style.display = "block";
    popup.style.display = "block";
}

function hidePopup() // closing bg and popup
{
    var popupBackground = document.getElementById("popupBackground");
    var popup = document.getElementById("popup");

    popupBackground.style.display = "none";
    popup.style.display = "none";
}



// <------------INPUT TYPE FOR UPLOADING FILES----------------->
var alertTriggered = false; // whether alert has been triggered

function showFileInput(type) 
{
  var fileInput = document.createElement("input");
  fileInput.type = "file";

  if (type === "video") 
  {
    fileInput.accept = "video/*";
  } 
  else if (type === "audio") 
  {
    fileInput.accept = "audio/*";
  } 
  else if (type === "book") 
  {
    fileInput.accept = ".pdf";
  }

  fileInput.addEventListener("change", function () 
  {
    if (!validateFileType(fileInput, type)) //when not supported file is chosen
    {
      if (!alertTriggered) //and checker which checks whether alert trigered or not
      {
        alert("Please choose an appropriate file type.");
        alertTriggered = true; // setting it to true.
        setTimeout(function () //adding cooldown for a alert bool
        {
          alertTriggered = false; // Reset the flag after a short delay
        }, 50);
      }
      return;
    }

    // alert for finish
    alert("File is uploaded!");
    hidePopup(); // popup dissapears
  });

  fileInput.click(); ///opening window for file selection
}

function validateFileType(fileInput, type) // file extension validation
{
  var allowedExtensions = []; // creating array for extensions

  if (type === "video") 
  {
    allowedExtensions = ["mp4", "mov", "avi"]; // customizable
  } 
  else if (type === "audio") 
  {
    allowedExtensions = ["mp3", "wav", "ogg", "m4a"];// customizable
  } 
  else if (type === "book") 
  {
    allowedExtensions = ["pdf"]; // customizable
  }

  var fileName = fileInput.value.split('.').pop().toLowerCase();
  if (!allowedExtensions.includes(fileName)) 
  {
    if (!alertTriggered) {
      alert("Please choose an appropriate file type.");
      alertTriggered = true; // Set the flag to true after the first alert
      setTimeout(function () 
      {
        alertTriggered = false; // Reset the flag after a short delay
      }, 50);
    }
    return false;
  }

  return true;
}





