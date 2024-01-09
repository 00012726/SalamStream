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
function showFileInput(type) {
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

    fileInput.addEventListener("change", function() 
    {
      // Handle file upload logic here
      alert("File uploaded successfully!");
      hidePopup();
    });

    fileInput.click();
}