document.addEventListener('DOMContentLoaded', function () {
    var startYear = 2004; 
    var endYear = 2022; 
    var startYearSelect = document.getElementById('start_year');
    var endYearSelect = document.getElementById('end_year');

    for (var year = startYear; year <= endYear; year++) {
        startYearSelect.options[startYearSelect.options.length] = new Option(year, year);
        endYearSelect.options[endYearSelect.options.length] = new Option(year, year);
    }

    startYearSelect.value = startYear;
    endYearSelect.value = endYear;

    startYearSelect.addEventListener('change', function () {
        adjustEndYearOptions();
    });

    function adjustEndYearOptions() {
        var selectedStartYear = parseInt(startYearSelect.value);
        endYearSelect.innerHTML = ''; // Clear existing options in end_year
        for (var year = selectedStartYear; year <= endYear; year++) {
            endYearSelect.options[endYearSelect.options.length] = new Option(year, year);
        }
        endYearSelect.value = endYear; // Set the end year to match the start year by default
    };

    startYearSelect.value = 2014;
    adjustEndYearOptions(); // Adjust end year options initially
});