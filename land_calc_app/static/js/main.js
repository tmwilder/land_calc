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
 'jqplot/jquery.jqplot',
 'js/app/bar_chart',
],
function(jquery, jqplot, bar_chart) {
    //jQuery, canvas and the app/sub module are all
    //loaded and can be used here now.

    function get_odds(deck, card_cost, on_the_play){
        var ajax_data = {
            deck: deck,
            card_cost: card_cost,
            on_the_play: on_the_play
        };
        ajax_data = JSON.stringify(ajax_data);
        $.ajax({
            type: "GET",
            url: "/get_odds/",
            data: $.param({data: ajax_data}),
            dataType: "json",
            success: bar_chart
        });
    }

    function get_deck(){
        var white = $("#deck_contents #white_count").val();
        var blue = $("#deck_contents #blue_count").val();
        var black = $("#deck_contents #black_count").val();
        var red = $("#deck_contents #red_count").val();
        var green = $("#deck_contents #green_count").val();
        var colorless = $("#deck_contents #colorless_count").val();

        var total_cards = $("#total_cards").val()

        var total_lands = 0;
        cards = {w:white, u:blue, b:black, r:red, g:green, c:colorless};
        var deck = {};
        for (var key in cards) {
            if (cards[key]){
                var count = parseInt(cards[key]);
                total_lands = total_lands + count;
                deck[key] = count;
            }
        };

        deck.s = total_cards - total_lands;

        return deck;
    }

    function get_cost(){
        var white = $("#mana_cost #white_count").val();
        var blue = $("#mana_cost #blue_count").val();
        var black = $("#mana_cost #black_count").val();
        var red = $("#mana_cost #red_count").val();
        var green = $("#mana_cost #green_count").val();
        var colorless = $("#mana_cost #colorless_count").val();

        var card_cost = {};
        if (white) {card_cost.w = white};
        if (blue) {card_cost.u = blue};
        if (black) {card_cost.b = black};
        if (red) {card_cost.r = red};
        if (green) {card_cost.g = green};
        if (colorless) {card_cost.c = colorless};

        return card_cost;
    }

    function get_play_status(){
        return $("#on_the_play").val() === "play" ? true: false;
    }

    function onGetOdds(){
        var deck = get_deck();
        var card_cost = get_cost();
        var on_the_play = get_play_status();
        get_odds(deck, card_cost, on_the_play);
    }
    existing_plot = undefined;
    $("#get_odds").on('click', onGetOdds);
    $(window).resize(function(){
        if (existing_plot !== undefined){
            existing_plot.replot();
        }
    });
});