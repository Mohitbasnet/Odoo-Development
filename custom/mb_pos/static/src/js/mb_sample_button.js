odoo.define("mb_pos.MohitSampleButton", function(require) {
"use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registeries = require("point_of_sale.Registries")
    const { useListener } = require("@web/core/utils/hooks");
    class MohitSampleButton extends PosComponent {

        setup(){
            super.setup();
            useListener("click",this.mb_sample_button_click );
        }

        mb_sample_button_click(){
            console.log("Hello this is button click event pressed")
        }


    }
    MohitSampleButton.template = "MohitSampleButton";
    ProductScreen.addControlButton({
        component: MohitSampleButton,
        position: ["before", "OrderlineCustomerNoteButton"],
    });

    Registeries.Component.add(MohitSampleButton);
    return MohitSampleButton;
});