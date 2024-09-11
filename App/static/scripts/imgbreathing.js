document.querySelectorAll('.hexagon-img').forEach(function(img) {
    img.addEventListener('mouseover', function() {
        img.style.animationPlayState = 'paused';
    });
    img.addEventListener('mouseout', function() {
        img.style.animationPlayState = 'running';
    });
});
