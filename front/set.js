// Define the base directory where your images are located
var baseDirectory = "C:\\Users\\Home\\PycharmProjects\\pythonSetGame\\front\\Set images\\";

// Array to keep track of downloaded images
var downloadedImages = [];

// Function to display the selected image
function showImage() {

    // Check if the maximum number of downloaded images (13) has been reached
    if (downloadedImages.length >= 13) {
        alert("You can only download up to 13 cards.");
        return;
    }
    // Get the selected values of the radio buttons
    var number = getSelectedValue("selected-number");
    var shape = getSelectedValue("selected-shape");
    var color = getSelectedValue("selected-color");
    var filling = getSelectedValue("selected-filling");

    // Check if any of the values are empty
    if (number === "" || shape === "" || color === "" || filling === "") {
        alert("Please select values for all attributes.");
        return; // Exit the function early if any value is empty
    }

    // Generate the image ID based on the selected values
    var imageId = number + shape + color + filling;

    // Check if the image has already been downloaded
    if (downloadedImages.includes(imageId)) {
        alert("This image has already been downloaded.");
        return;
    }

    // Construct the image path
    var imagePath = baseDirectory + imageId + ".PNG";
    console.log("Image Path:", imagePath);

    // Create a new Image element
    var img = new Image();
    img.src = imagePath;
    img.alt = "Set card " + imageId;
    img.className = "set-card-images";

    // Add event listener to handle image load
    img.onload = function() {
        console.log("Image loaded successfully:", img.src);
        // Append the image to the container when image is loaded
        var container = document.getElementById("imageContainer");
        container.appendChild(img);

        // Create a delete button for the image
        var deleteButton = document.createElement("button");
        deleteButton.textContent = "X";
        deleteButton.className = "delete-button";
        deleteButton.onclick = function() {
            container.removeChild(img); // Remove the image when delete button is clicked
            container.removeChild(deleteButton); // Remove the delete button
            // Remove the image ID from the downloaded images array
            var index = downloadedImages.indexOf(imageId);
            if (index !== -1) {
                downloadedImages.splice(index, 1);
            }
        };
        container.appendChild(deleteButton);

        // Add the image ID to the downloaded images array
        downloadedImages.push(imageId);
    };

    // Add error handling for image loading
    img.onerror = function() {
        console.error("Error loading image:", imagePath);
        alert("Error loading image: " + imagePath);
    };

    // Reset the form
    resetForm();
}

// Function to get the selected value of a radio button group
function getSelectedValue(groupName) {
    var radioButtons = document.getElementsByName(groupName);
    for (var i = 0; i < radioButtons.length; i++) {
        if (radioButtons[i].checked) {
            return radioButtons[i].value;
        }
    }
    return ""; // Return empty string if no radio button is checked
}

// Function to reset form
function resetForm() {
    // Uncheck all radio buttons
    var radioButtons = document.querySelectorAll("input[type='radio']:checked");
    radioButtons.forEach(function(radioButton) {
        radioButton.checked = false;
    });
}

function trouveSet() {
    console.log(downloadedImages);
}

// Function to reset everything
function resetEverything() {
    // Uncheck all radio buttons
    var radioButtons = document.querySelectorAll("input[type='radio']:checked");
    radioButtons.forEach(function(radioButton) {
        radioButton.checked = false;
    });

    // Remove all images
    var container = document.getElementById("imageContainer");
    container.innerHTML = ""; // This removes all child elements

    // Clear downloaded images array
    downloadedImages = [];
}