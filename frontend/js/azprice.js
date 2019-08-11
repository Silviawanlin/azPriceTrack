function search(){
    var searchContent = $("#searchContent").val();
    var prefix = searchContent.substring(0,4).toLowerCase();
    console.log(prefix);
    if(prefix === "http")
    {
        //http://vm76.com:8000/price/get?url=https://www.amazon.com/gp/product/B01HOS31B0?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=VJQJJSGTMRT23K2K6S8T
        $.ajax({
            url: "http://vm76.com:8000/price/get?url=" + $("#searchContent").val(),
            type: 'GET',
            success: function(data){
                // data = JSON.parse(data);
                console.log(data);
                var myArr= data.historicalPrices;
                var htm=$('#data');
                for(var i=0;i<myArr.length;i++){
                    htm += '<tr><td>' + myArr[i].date + '</td><td>'
                            + myArr[i].price + '</td><td>'
                            + data.title+ '</td><td>';
                            // + myArr[i].email+'</td><td>'
                            // + myArr[i].phone+'</td><td>';
                }
                htm += '</tbody></table>';
                $("#data").append(htm);
            }
        });
    }
    else
    {
        alert("A URL, please...");
    }
}