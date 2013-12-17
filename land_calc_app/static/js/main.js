requirejs.config({
    //By default load any module IDs from js/lib
    baseUrl: '/static',
    //except, if the module ID starts with "app",
    //load it from the js/app directory. paths
    //config is relative to the baseUrl, and
    //never includes a ".js" extension since
    //the paths config could be for a directory.
    paths: {}
});

// Start the main app logic.
requirejs([
 'js/lib/jquery-2.0.3.min',
 'js/app/get_odds',
 'js/lib/addthis',
 'js/app/nav_tab',
],
function(jquery, onGetOdds) {
    //jQuery, canvas and the app/sub module are all
    //loaded and can be used here now.

    $("#get_odds").click(onGetOdds);

    $(window).resize(function(){
        if (existing_plot !== undefined){
            existing_plot.replot();
        }
    });

    existing_plot = undefined;

});