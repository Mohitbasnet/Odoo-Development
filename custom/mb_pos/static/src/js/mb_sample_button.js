odoo.define("mb_pos.MohitSampleButton", function(require) {
"use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registeries = require("point_of_sale.Registries")
    class MohitSampleButton extends PosComponent {



    }
    MohitSampleButton.template = "MohitSampleButton";
    ProductScreen.addControlButton({
        component: MohitSampleButton,
        position: ["before", "OrderlineCustomerNoteButton"],
    });

    Registeries.Component.add(MohitSampleButton);
    return MohitSampleButton;
});