function get_next_level(server_data, method, url){
    $.ajax({
        url: url,
        type: method,
        data: JSON.stringify(server_data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data){
        $("#content").html(data);
            console.log("SUCCESS: " + JSON.stringify(data));
        },
        error: function(data){
            $("#content").html("Failed to load data. " + JSON.stringify(data));
            console.log("ERROR: " + JSON.stringify(data));
        },
    });
}