
// Image Breathing

document.querySelectorAll('.hexagon-img').forEach(function(img) {
    img.addEventListener('mouseover', function() {
        img.style.animationPlayState = 'paused';
    });
    img.addEventListener('mouseout', function() {
        img.style.animationPlayState = 'running';
    });
});

document.getElementById('saved-recipes-btn').addEventListener('click', function(event) {
    event.preventDefault(); 
    window.location.href = '{% url "saved_recipes" %}'; 
});

document.getElementById('explore-recipes-btn').addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = '{% url "explore_recipes" %}';
});

document.getElementById('groceries-btn').addEventListener('click', function(event) {
    event.preventDefault();
    window.location.href = '{% url "groceries" %';
});

