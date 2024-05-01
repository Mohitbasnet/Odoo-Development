odoo.define("mb_pos.MohitSampleButton", function(require) {
"use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registeries = require("point_of_sale.Registries")
    const { useListener } = require("@web/core/utils/hooks");
    const  core  = require("web.core");
    var _t = core._t;


    class MohitSampleButton extends PosComponent {

        setup(){
            super.setup();
            useListener("click",this.mb_sample_button_click );
        }

        async mb_sample_button_click(){

            


            // var result = await this.rpc({
            //     'model':"res.lang",
            //     "method":"search_read",
            //     "args":[[],['id','name','code']],
            // })
           

            // RPC CALL
            var result = await this.rpc({
                route: "/pos/rpc/example",
                params: {}
            })
            
           

            result.forEach(function(value){
                console.log("Record--->",value);
            })

            console.log(result);

            //  Sound pop up
            // this.showPopup("ErrorPopup", {
            //     title: _t("Error message"),
            //     body: this.env._t("The simple Error message"),
            // });

            // // Confirm popup
            // var { confirmed }= await this.showPopup("ConfirmPopup",{
            //     title: _t("Confirm Popup"),
            //     body: _t("Are you sure to continue?"),
            //     confirmText: _t("Yes"),
            //     cancelText: _t("No")
            // });
            // // if (confirmed){
            // //     console.log("clicked to Yes button")
            // // }else{
            // //     console.log("clicked to No button")
            // // }
            
            // // offline error popup
            // this.showPopup("OfflineErrorPopup",{
            //     title: _t("Mohit Error"),
            //     body: this.env._t("Hey this is the test popup screen okay don't take it serious!")
            // });

            // // Choice popup
            // var { confirmed, payload: selectedOption } = await this.showPopup("SelectionPopup",{
            //     title: ("Are you a good python developer."),
            //     list:[{'id':0,'label': _t("Yes "),'item':"You pressed yes"},
            //       {'id':1,'label': _t("No"),'item':"You pressed No"},
            //       {'id':2,'label': _t("In confusion"),'item':"you pressed in confusion"}]
            // });

            // // console.log(confirmed);
            // // console.log(selectedOption);
            
            // const info = await this.env.pos.getClosePosInfo();
            // this.showPopup("ClosePosPopup",{
            //     info: info,
            //     KeepBehind: true
            // })

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