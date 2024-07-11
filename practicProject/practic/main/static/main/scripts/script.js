document.addEventListener('DOMContentLoaded', function() {
    var slider = document.getElementById('salary-slider');
    var output = document.getElementById('current-salary');

    slider.addEventListener('input', function() {
        output.textContent = this.value;
    });
});