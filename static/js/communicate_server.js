function connection_to_server(server_data, method, url){
    var response = null;
    $.ajax({
        async: false,
        url: url,
        type: method,
        data: JSON.stringify(server_data),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(res){
            response = res
        },
    });
    return response
}