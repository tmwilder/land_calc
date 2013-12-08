define(['js/lib/jquery-2.0.3.min', 'js/app/bar_chart'],
function(jquery, bar_chart){
    function _refresh_odds(deck, card_cost, on_the_play){
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

    function _get_deck(){
        // Single Colored Lands
        var white = $("#deck_contents #white_count").val();
        var blue = $("#deck_contents #blue_count").val();
        var black = $("#deck_contents #black_count").val();
        var red = $("#deck_contents #red_count").val();
        var green = $("#deck_contents #green_count").val();
        var colorless = $("#deck_contents #colorless_count").val();

        // Duals
        var azorius = $("#deck_contents #azorius_count").val();
        var boros = $("#deck_contents #boros_count").val();
        var dimir = $("#deck_contents #dimir_count").val();
        var golgari = $("#deck_contents #golgari_count").val();
        var gruul = $("#deck_contents #gruul_count").val();
        var izzit = $("#deck_contents #izzit_count").val();
        var orzhov = $("#deck_contents #orzhov_count").val();
        var rakdos = $("#deck_contents #rakdos_count").val();
        var selesnya = $("#deck_contents #selesnya_count").val();
        var simic = $("#deck_contents #simic_count").val();

        var total_cards = $("#total_cards").val()

        cards = {
            w:white,
            u:blue,
            b:black,
            r:red,
            g:green,
            c:colorless,
            wu:azorius,
            wr:boros,
            ub:dimir,
            bg:golgari,
            rg:gruul,
            ur:izzit,
            wb:orzhov,
            br:rakdos,
            wg:selesnya,
            ug:simic
        };

        var total_lands = 0;
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

    function _get_cost(){
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

    function _get_play_status(){
        return $("#on_the_play").val() === "play" ? true: false;
    }

    return function onGetOdds(){
        var deck = _get_deck();
        var card_cost = _get_cost();
        var on_the_play = _get_play_status();
        _refresh_odds(deck, card_cost, on_the_play);
    }
});