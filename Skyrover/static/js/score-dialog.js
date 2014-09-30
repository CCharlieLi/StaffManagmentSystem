        //dialog
        $(document).ready(function() {
            
            $("#mws-jui-dialog-edit").dialog({
                autoOpen: false, 
                title: "Edit Score", 
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
            $("#form_username").attr("value","");
            $("#form_scorenum").attr("value","");
            editid = eid
            $.getJSON('/API/REST/employees/'+editid,function(result,status){
                //alert(result.Name);
                $("#form_ID").attr("value",editid);
                $("#form_username").attr("value",result.UserName);
                $("#form_scorenum").attr("value",result.Score);
                //levelmaster = result.levelMaster;
            });
            //alert(editid)
        };

        //REST delete
        var urlstr;
        function search()
        {
            window.location="/manage/scorelist?SearchName="+$("#searchtext").attr('value'); 
        };

        