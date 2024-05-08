document.addEventListener("DOMContentLoaded", function() {

    var addToCartButton = document.querySelector(".addCart");
    var sellerInfoContainer = document.querySelector(".sellerInfo");
    var sellerInfoDisplayStyle = window.getComputedStyle(sellerInfoContainer).display;
    addToCartButton.addEventListener("click", function(event) {
        event.preventDefault();

        if (sellerInfoDisplayStyle === "none") {
            sellerInfoContainer.style.display = "block";
        } else {
            sellerInfoContainer.style.display = "none";
        }
    });
});


// the policey terms buttons function
const aboutButton = document.getElementById('aboutButton');
const aboutContainer = document.getElementById('aboutContainer');
const togglePostageButton = document.getElementById('togglePostageButton');
const togglePostageContainer = document.getElementById('postageContainer');

togglePostageContainer.style.display = 'none';

aboutButton.addEventListener('click', function() {
    
    aboutButton.style.backgroundColor = '#DBDBDB';
    aboutButton.querySelector('h2').style.color = '#1D4ED8'; 

    togglePostageButton.style.backgroundColor = '';
    togglePostageButton.querySelector('h2').style.color = '#6C6C6C'; 

    aboutContainer.style.display = 'block';
    togglePostageContainer.style.display = 'none';
});

togglePostageButton.addEventListener('click', function() {
    togglePostageButton.style.backgroundColor = '#DBDBDB'; 

    togglePostageButton.querySelector('h2').style.color = '#1D4ED8'; 
    aboutButton.style.backgroundColor = ''; 

    aboutButton.querySelector('h2').style.color = '#6C6C6C'; 
    aboutContainer.style.display = 'none';
    togglePostageContainer.style.display = 'block';
});



// Product sold section

    document.getElementById("buyButton").addEventListener("click", function() {
        var quantity = parseInt(document.getElementById("quantityInput").value);
        var availableCount = parseInt(document.getElementById("availableCount").textContent);
        var soldCount = parseInt(document.getElementById("soldCount").textContent);

        if (quantity > availableCount) {
            alert("Sorry, only " + availableCount + " available.");
        } else {
            soldCount += quantity;
            availableCount -= quantity;
            document.getElementById("soldCount").textContent = soldCount;
            document.getElementById("availableCount").textContent = availableCount + " available";

            if (availableCount === 0) {
                
                document.querySelector(".availables").innerHTML = "<h3>product Has been Sold Out</h3>";
                document.getElementById("buyButton").disabled = true; 
            }

        }
    });
