var menuIcon = document.querySelector(".menuIcon");
var sidebar = document.querySelector(".sidebar");
var container = document.querySelector(".container");

menuIcon.onclick = function()
{
    sidebar.classList.toggle("smallSidebar");
    container.classList.toggle("largeContainer");
}

function showPopup() 
{
    var popupBackground = document.getElementById("popupBackground");
    var popup = document.getElementById("popup");

    popupBackground.style.display = "block";
    popup.style.display = "block";
}

function hidePopup() 
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
    if (!validateFileType(fileInput, type)) 
    {
      if (!alertTriggered) 
      {
        alert("Please choose an appropriate file type.");
        alertTriggered = true; // Set the flag to true after the first alert
        setTimeout(function () 
        {
          alertTriggered = false; // Reset the flag after a short delay
        }, 50);
      }
      return;
    }

    // Handle file upload logic here
    alert("File uploaded successfully!");
    hidePopup();
  });

  fileInput.click();
}

function validateFileType(fileInput, type) 
{
  var allowedExtensions = [];

  if (type === "video") 
  {
    allowedExtensions = ["mp4", "mov", "avi"];
  } 
  else if (type === "audio") 
  {
    allowedExtensions = ["mp3", "wav", "ogg", "m4a"];
  } 
  else if (type === "book") 
  {
    allowedExtensions = ["pdf"];
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





