        //dialog
        $(document).ready(function() {
            $("#mws-jui-dialog-new").dialog({
                autoOpen: false, 
                title: "New Level", 
                modal: true, 
                width: "640", 
                buttons: [{
                        text: "Close", 
                        click: function() {
                            $( this ).dialog( "close" );
                        }}]
            });

            $(".mws-jui-dialog-mdl-btn-new").bind("click", function(event) {
                $("#mws-jui-dialog-new").dialog("option", {modal: true}).dialog("open");
                event.preventDefault();
            });

            $("#mws-jui-dialog-edit").dialog({
                autoOpen: false, 
                title: "Edit Level", 
                modal: true, 
                width: "640", 
                buttons: [{
                        text: "Close", 
                        click: function() {
                            $( this ).dialog( "close" );
                        }}]
            });

            $(".mws-jui-dialog-mdl-btn-edit").bind("click", function(event) {
                $("#mws-jui-dialog-edit").dialog("option", {modal: true}).dialog("open");
                event.preventDefault();
            });
        });

        //REST get
        var editid = -1;
        function changeID(eid)
        {   
            $("#form_ID").attr("value","");
            $("#form_levelname").attr("value","");
            
            editid = eid
            $.getJSON('/API/REST/levels/'+editid,function(result,status){
                //alert(result.Name);
                $("#form_ID").attr("value",editid);
                $("#form_levelname").attr("value",result.Levelname);

                //levelmaster = result.levelMaster;
            });
            //alert(editid)
        };

        //REST delete
        var urlstr;
        function search()
        {
            window.location="/manage/levellist?SearchName="+$("#searchtext").attr('value'); 
        };

        