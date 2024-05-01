odoo.define("mb_pos.MohitClearButton", function(require) {
    "use strict";
    
        const PosComponent = require("point_of_sale.PosComponent");
        const ProductScreen = require("point_of_sale.ProductScreen");
        const Registeries = require("point_of_sale.Registries")
        const { useListener } = require("@web/core/utils/hooks");

    
        class MohitClearButton extends PosComponent {
    
            setup(){
                super.setup();
                useListener("click",this.mb_clear_all_lines );
            }
    
            mb_clear_all_lines(){

               console.log("mb_clear_all_lines method called...")
               var current_order = this.env.pos.get_order();
               console.log(current_order);
               current_order.orderlines.filter(line=> line.get_product()).forEach(single_line=> current_order.remove_orderline(single_line));
            }
    
    
        }
        MohitClearButton.template = "MohitClearButton";
        ProductScreen.addControlButton({
            component: MohitClearButton,
            position: ["after", "OrderlineCustomerNoteButton"],
        });
    
        Registeries.Component.add(MohitClearButton);
        return MohitClearButton;
    });