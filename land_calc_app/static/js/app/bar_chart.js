define(['js/lib/jquery-2.0.3.min', 'jqplot/jquery.jqplot'],
function(jquery, jqplot){
    require([
        'jqplot/jquery.jqplot',
        'jqplot/plugins/jqplot.barRenderer.min',
        'jqplot/plugins/jqplot.categoryAxisRenderer.min',
        'jqplot/plugins/jqplot.pointLabels.min'
    ]);
    return function(data){
        if (existing_plot !== undefined){
            existing_plot.destroy();
        }
        // Can specify a custom tick Array.
        // Ticks should match up one for each y value (category) in the series.
        var ticks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        var yticks = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0];
        var plot1 = $.jqplot('bar_chart', [data], {
            title: "Odds of Drawing Sufficient Lands to Cast a Spell by Turn X",
            // The "seriesDefaults" option is an options object that will
            // be applied to all series in the chart.
            seriesDefaults:{
                renderer:$.jqplot.BarRenderer,
                rendererOptions: {fillToZero: true},
                pointLabels: { show:true, formatString: "%#.2f"} 
            },
            axes: {
                // // Use a category axis on the x axis and use our custom ticks.
                xaxis: {
                    renderer: $.jqplot.CategoryAxisRenderer,
                    ticks: ticks,
                    label: "Turns Progressed",
                    tickOptions: {formatString: "%d"}
                },
                // // Pad the y axis just a little so bars can get close to, but
                // // not touch, the grid boundaries.  1.2 is the default padding.
                yaxis: {
                    pad: 1.05,
                    ticks: yticks,
                    label: "Odds of Casting Your Spell"
                }
            }
        });
        existing_plot = plot1;
    }
});
