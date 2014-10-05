        //dialog
        $(document).ready(function() {
            $("#mws-jui-dialog-new").dialog({
                autoOpen: false, 
                title: "New Group", 
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
                title: "Edit Group", 
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
        var status;
        function changeID(eid)
        {   
            $("#form_ID").attr("value","");
            $("#form_groupname").attr("value","");
            $("#form_groupmaster").attr("value","");
            $("#form_groupmaster").attr("selected","");
            
            editid = eid
            $.getJSON('/API/REST/groups/'+editid,function(result,status){
                //alert(result.Name);
                $("#form_ID").attr("value",editid);
                $("#form_groupname").attr("value",result.Name);
                $("#form_groupmaster").attr("text",result.GroupMaster);
                $("#form_groupmaster").attr("selected","selected");
                //groupmaster = result.GroupMaster;
                
            });
            //alert(editid)
        };

        //REST delete
        var urlstr;
        function search()
        {
            window.location="/manage/grouplist?SearchName="+$("#searchtext").attr('value'); 
        };

        