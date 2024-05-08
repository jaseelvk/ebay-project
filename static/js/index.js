function setActive(link) {
    
    var links = document.querySelectorAll("#categorySelect .container ul li a");
    links.forEach(function(a) {
        a.classList.remove("active");
    });
   
    link.classList.add("active");
}


// slider function
    document.addEventListener('DOMContentLoaded', function() {
        const categories = document.querySelectorAll('#e_platform section.wrapper div.e_container');
    
        categories.forEach(category => {
            const leftArrow = category.querySelector('.shop-left');
            const rightArrow = category.querySelector('.shop-right');
            const productList = category.querySelector('ul');
    
            let isDragging = false;
            let startX;
            let scrollLeft;
    
            const scrollAmount = 300;
    
            function scrollProductList(direction) {
                if (direction === 'left') {
                    productList.scrollLeft -= scrollAmount;
                } else if (direction === 'right') {
                    productList.scrollLeft += scrollAmount;
                }
                updateButtonVisibility();
            }
    
            function updateButtonVisibility() {
                leftArrow.style.display = productList.scrollLeft <= 0 ? 'none' : 'block';
                rightArrow.style.display = productList.scrollLeft >= (productList.scrollWidth - productList.clientWidth) ? 'none' : 'block';
            }
    
            leftArrow.addEventListener('click', function() {
                scrollProductList('left');
            });
    
            rightArrow.addEventListener('click', function() {
                scrollProductList('right');
            });
    
            productList.addEventListener('mousedown', (e) => {
                isDragging = true;
                startX = e.pageX - productList.offsetLeft;
                scrollLeft = productList.scrollLeft;
            });
    
            productList.addEventListener('mouseleave', () => {
                isDragging = false;
            });
    
            productList.addEventListener('mouseup', () => {
                isDragging = false;
            });
    
            productList.addEventListener('mousemove', (e) => {
                if (!isDragging) return;
                e.preventDefault();
                const x = e.pageX - productList.offsetLeft;
                const walk = (x - startX) * 1;
                productList.scrollLeft = scrollLeft - walk;
            });
    
            updateButtonVisibility();
        });
    });

    // Search button Function

    document.getElementById('searchButton').addEventListener('click', function() {
        document.getElementById('searchForm').submit();
    });


// the filetr category chnageing function

document.addEventListener('DOMContentLoaded', function() {
    var optionsSelect = document.getElementById('options');
    var selectedCategory = "{{ selected_category }}"; 
    
    if (selectedCategory) {
        for (var i = 0; i < optionsSelect.options.length; i++) {
            if (optionsSelect.options[i].value === selectedCategory) {
                optionsSelect.options[i].selected = true;
                break;
            }
        }
    }
    
   
    optionsSelect.addEventListener('change', function(event) {
        
        this.form.submit();
    });
});
//  auto-sliding
let currentIndex = 0; 
const slides = document.querySelectorAll('.bnContainer > .bnItem'); 
const totalSlides = slides.length;
const intervalTime = 2000; 
const transitionTime = 1000; 

function showSlide(index) {
    
    slides.forEach((slide, i) => {
        if (i === index) {
            slide.style.display = 'block';
        } else {
            slide.style.display = 'none';
        }
    });
}

function nextSlide() {
    currentIndex++;
    if (currentIndex >= totalSlides) {
        currentIndex = 0; 
    }
    showSlide(currentIndex);
}


let slideInterval = setInterval(nextSlide, intervalTime);


document.getElementById('banner').addEventListener('mouseenter', () => {
    clearInterval(slideInterval);
});


document.getElementById('banner').addEventListener('mouseleave', () => {
    slideInterval = setInterval(nextSlide, intervalTime);
});


showSlide(currentIndex);


//wish list items

$(document).ready(function() {
    
    $(document).on("click", ".add-to-wishList:not(.disabled)", function() {
        var _pid = $(this).attr('data-product-id');
        var _vm = $(this);
        var addToWishlist = !_vm.hasClass('hidden');
        var ajaxUrl = addToWishlist ? "/add-wishlist/" : "/remove-wishlist/";
        _vm.addClass('disabled');

        // Ajax
        $.ajax({
            url: ajaxUrl,
            data: {
                product: _pid
            },
            dataType: 'json',
            success: function(res) {
                console.log("Success:", res);
                if (res.bool === true) {
                    if (addToWishlist) {
                        _vm.addClass('hidden');
                        _vm.siblings('.add-to-wishList-rounded-button').removeClass('hidden');
                    } else {
                        _vm.removeClass('hidden');
                        _vm.siblings('.add-to-wishList-rounded-button').addClass('hidden');
                    }
                } else {
                    console.error("Error: Unexpected response from server");
                }
            },
            error: function(xhr, status, error) {
                console.error("Error:", error);
            },
            complete: function() {
                _vm.removeClass('disabled');
            }
        });
    });

    
    $(document).on("click", ".add-to-wishList-rounded-button:not(.disabled)", function() {
        var _pid = $(this).attr('data-product-id');
        var _vm = $(this);
        _vm.addClass('disabled');
    
        // Ajax
        $.ajax({
            url: "/remove-wishlist/",
            data: {
                product: _pid
            },
            dataType: 'json',
            success: function(res) {
                console.log("Success:", res);
                if (res.bool === true) {
                    
                    _vm.closest('li').find('.add-to-wishList').removeClass('hidden');

                   
                    _vm.addClass('hidden');
                } else {
                    console.error("Error: Unexpected response from server");
                }
            },
            error: function(xhr, status, error) {
                console.error("Error:", error);
            },
            complete: function() {
                _vm.removeClass('disabled');
            }
        });
    });
});
