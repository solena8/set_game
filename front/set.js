// Define the base directory where your images are located
var baseDirectory = "/Set images/";

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


function showFoundSetImages(data) {
    // Séparer les 3 IDs de cartes récupérés puis construire le chemin de l'image
    var imagePaths = data.map(function(cardId) {
        // Construct the image path
        return baseDirectory + cardId + ".PNG";
    });

    // Loop through each image path and create an image element for it
    imagePaths.forEach(function(imagePath) {
        // Create a new Image element
        var img = new Image();
        img.src = imagePath;
        img.alt = "Set card " + imagePath; // Use imagePath here to ensure unique alt text for each image
        img.className = "set-card-images";

        // Add event listener to handle image load
        img.onload = function() {
            console.log("Image loaded successfully:", img.src);
        };

        // Add error handling for image loading
        img.onerror = function() {
            console.error("Error loading image:", imagePath);
            alert("Error loading image: " + imagePath);
        };

        // Append the image element to the document body or another container
        document.getElementById("resultImages").appendChild(img);
    });
}


function trouveSet() {
    const cards = (downloadedImages)
    //["1ORH","2OVP","3OMV","1ORP"];//
    console.log(downloadedImages);
        
    // Function to format cards array for API URL
    const formatCards = cards.join(',');

    
     // Define the API URL
     const apiUrl = `http://127.0.0.1:8000/cards/${formatCards}`;
     console.log(apiUrl);


    // Make a GET request
    fetch(apiUrl)
    .then(response => {
        if (!response.ok) {
        throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Log the data received from the API
        // Call the function to display images
        showFoundSetImages(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
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