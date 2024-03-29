$(function() {
    "use strict";

    function e(e, n) {
        for (var t = n.length, o = 0; t >= o; o++) {
            var s = n[o].title;
            if (s === e) return n[o]
        }
        return null
    }
    var n = "#cy2",
        network = networks2[Object.keys(networks2)[0]],
        style = styles2[0];
    $(n).cytoscape({
        layout: {
            name: "preset",
            padding: 10
        },
        boxSelectionEnabled: !0,
        ready: function() {
            window.cy = this, 
                    cy.load(network.elements), console.log(network);
                    console.log(style);
                    var o = e("default", style);
                    null === o && (o = style), cy.style().fromJson(o.style).update()
                
        }
    })
});