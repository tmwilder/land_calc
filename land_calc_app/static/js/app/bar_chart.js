define([
    'js/lib/jquery-2.0.3.min',
    'jqplot/jquery.jqplot',
    'jqplot/plugins/jqplot.barRenderer.min',
    'jqplot/plugins/jqplot.categoryAxisRenderer.min',
    'jqplot/plugins/jqplot.pointLabels.min',
    ], function(jquery){
    return function(data){
        // Can specify a custom tick Array.
        // Ticks should match up one for each y value (category) in the series.
        var ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        var plot1 = $.jqplot('bar_chart', [data], {
            // The "seriesDefaults" option is an options object that will
            // be applied to all series in the chart.
            seriesDefaults:{
                renderer:$.jqplot.BarRenderer,
                rendererOptions: {fillToZero: true}
            },
            axes: {
                // // Use a category axis on the x axis and use our custom ticks.
                xaxis: {
                    renderer: $.jqplot.CategoryAxisRenderer,
                    ticks: ticks
                },
                // // Pad the y axis just a little so bars can get close to, but
                // // not touch, the grid boundaries.  1.2 is the default padding.
                yaxis: {
                    pad: 1.05,
                    tickOptions: {formatString: '%#.3f'}
                }
            }
        });
    }
});