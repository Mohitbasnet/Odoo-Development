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

        async mb_sample_button_click(){
            //  Sound pop up
            // this.showPopup("ErrorPopup", {
            //     title:"Error message",
            //     body:"The simple Error message",
            // });

            // Confirm popup
            // const { confirmed } = await this.showPopup("ConfirmPopup",{
            //     title:"Confirm Popup",
            //     body:"Are you sure to continue?",
            //     confirmText: "Yes",
            //     cancelText:"No"
            // });
            // if (confirm){
            //     console.log("clicked to Yes button")
            // }else{
            //     console.log("clicked to No button")
            // }
            
            // offline error popup
            // this.showPopup("OfflineErrorPopup",{
            //     title:"Mohit Error",
            //     body: "Hey this is the test popup screen okay don't take it serious!"
            // });

            // Choice popup
            // const { confirmed, payload: selectedOption } = await this.showPopup("SelectionPopup",{
            //     title:"Are you a good python developer.",
            // list:[{'id':0,'label':"Yes ",'item':"You pressed yes"},
            //       {'id':1,'label':"No",'item':"You pressed No"},
            //       {'id':2,'label':"In confusion",'item':"you pressed in confusion"}]
            // });

            // console.log(confirmed);
            // console.log(selectedOption);
            
            const info = await this.env.pos.getClosePosInfo();
            this.showPopup("ClosePosPopup",{
                info: info,
                KeepBehind: true
            })

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